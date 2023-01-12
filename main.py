import logging.config
import argparse
import textwrap
import datetime as dt
from time import sleep
from threading import Thread
from typing import Callable
#
import scheduler
import telebot
from scheduler import Scheduler
#
from conf import TOKEN, LOG_CONFIG
from holidays import HolyParser
from utils import *


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('Greetings_TGBot')


bot = telebot.TeleBot(TOKEN)  # создание экземпляра класса TeleBot и передача токена ему
run = True


class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    # Class will check whether the user is admin or creator in group or not
    key = 'is_chat_admin'

    def check(self, message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']


bot.add_custom_filter(IsAdmin())


@bot.message_handler(commands=['start'], chat_types=["private", "group"])
def start(message: telebot.types.Message):
    """Обработчик команды /start"""
    task = get_schedule(send_holidays, chat_id=message.chat.id)
    Thread(target=start_tasks, args=(task,), name='Periodicly_tasks').start()
    logger.info('Расписание запушено')
    bot.send_message(message.chat.id, 'Расписание запущено')


@bot.message_handler(commands=['help'], chat_types=["private", "group"])
def help_message(message: telebot.types.Message):
    """Обработчик команды /help"""
    bot.send_message(message.chat.id, 'тест для вывода на команду /help')


@bot.message_handler(commands=['stop'], chat_types=["private", "group"], is_chat_admin=True)
def stop_bot(message: telebot.types.Message):
    """Обработчик команды /stop"""
    # вариант до настройки фильтров. Пока оставил
    # if bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']:
    #     global run
    #     run = False
    #     bot.stop_bot()

    global run
    run = False
    bot.stop_bot()
    bot.send_message(message.chat.id, 'Бот остановлен')
    logger.info('Бот остановлен')


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message: telebot.types.Message):
    """Приветствие вошедших пользователей"""
    name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, f"Добро пожаловать, @{name}!")


def send_message_to_group(text: str, chat_id: int):
    """отправка сообщения в группу"""


# TASKS

def start_tasks(schedule: Scheduler):
    while True:
        schedule.exec_jobs()
        sleep(1)


def get_schedule(task: Callable, *, hour=10, minute=0, second=0, **kwargs):
    """Создаёт расписание и возвращает экземпляр класса Scheduler"""
    schedule = Scheduler()
    schedule.daily(dt.time(hour=hour, minute=minute, second=second), task, kwargs=kwargs)
    return schedule


def send_holidays(chat_id):
    parser = HolyParser()
    all_events = parser.get_all()
    message = dict_to_format_string(all_events)
    send_message_to_group(message, chat_id)


# Аргументы для запуска
def arg_parser():
    """Определяет аргументы"""
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent("""
                                     Telegram bot for telegram chat sun_it_people
                                     """))

    # добавляем аргументы:
    parser.add_argument('-t', '--token', action="store", default=None,
                        help='Bot token. By default is None.')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = arg_parser()

    # TODO: этот бред надо переписать
    if not args.token and not TOKEN:
        logger.error('Не введён токен бота! '
                     'Нужно прописать его в конфиге в переменную TOKEN, либо ввести, как аргумент: "-t TOKEN"')
    else:
        TOKEN = args.token or TOKEN

    try:
        bot.polling(none_stop=True)  # запуск с параметром "не останавливать работу"
    except KeyboardInterrupt:
        run = False
        bot.stop_bot()
        print('Остановлено пользователем')
