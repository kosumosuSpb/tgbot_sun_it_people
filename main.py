import logging.config
import datetime as dt
from time import sleep
from threading import Thread
from typing import Callable
#
import telebot
from scheduler import Scheduler
#
from conf import TOKEN, LOG_CONFIG
from holidays import HolyParser
from utils import *


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('GreeTG_Bot')


bot = telebot.TeleBot(TOKEN)  # создание экземпляра класса TeleBot и передача токена ему
run = True


# Обработчики команд
@bot.message_handler(commands=['start'], chat_types=["private", "group", "supergroup"])
def start(message: telebot.types.Message):
    """Обработчик команды /start"""
    task = set_schedule(send_morning_message, chat_id=message.chat.id)
    Thread(target=start_tasks, args=(task,), name='Periodically_tasks').start()
    logger.info('Расписание запущено')
    bot.send_message(message.chat.id, 'Расписание запущено')


@bot.message_handler(commands=['help'], chat_types=["private", "group", "supergroup"])
def help_message(message: telebot.types.Message):
    """Обработчик команды /help"""
    bot.send_message(message.chat.id, 'тест для вывода на команду /help')


@bot.message_handler(commands=['stop'], chat_types=["group", "supergroup"], is_chat_admin=True)
def stop(message: telebot.types.Message):
    """Обработчик команды /stop"""
    global run
    run = False
    bot.send_message(message.chat.id, f'Расписание остановлено пользователем '
                                      f'{message.from_user.first_name} ({message.from_user.username})')
    logger.info(f'Расписание остановлено пользователем {message.from_user.first_name} (@{message.from_user.username})')


@bot.message_handler(commands=['stop'], chat_types=["private"])
def stop(message: telebot.types.Message):
    """Обработчик команды /stop"""
    global run
    run = False
    bot.send_message(message.chat.id, f'Расписание остановлено пользователем '
                                      f'{message.from_user.first_name} ({message.from_user.username})')
    logger.info(f'Расписание остановлено пользователем {message.from_user.first_name} (@{message.from_user.username})')


@bot.message_handler(commands=['stop_bot'], chat_types=["private", "group", "supergroup"], is_chat_admin=True)
def stop_bot(message: telebot.types.Message):
    """Обработчик команды /stop_bot"""

    # TODO: переделать на нормальный фильтр
    if message.from_user.username != 'kosumosu':
        bot.send_message(message.chat.id, 'Доступ запрещён')

    global run
    run = False
    bot.send_message(message.chat.id, 'Бот остановлен')
    bot.stop_bot()
    logger.info('Бот остановлен')


@bot.message_handler(content_types=["new_chat_members"], chat_types=["group", "supergroup"])
def new_member(message: telebot.types.Message):
    """Приветствие вошедших пользователей"""
    # name = message.new_chat_members[0].first_name
    members = ', '.join([f'{member.first_name} (@{member.username})' for member in message.new_chat_members])
    logger.debug(f'New members: {members}')
    bot.send_message(message.chat.id, f"Добро пожаловать, {members}!")


@bot.message_handler(content_types=["left_chat_member"], chat_types=["group", "supergroup"])
def left_member(message: telebot.types.Message):
    """Уведомление о вышедшем пользователе"""
    member = message.left_chat_member
    bot.send_message(message.chat.id, f"{member.first_name} (@{member.username}) покинул(а) чат о_О")


def send_message_to_group(text: str, chat_id: int):
    """отправка сообщения в группу"""
    bot.send_message(chat_id, text)


# TASKS

def start_tasks(schedule: Scheduler):
    global run
    logger.debug(f'Расписание запущено в {dt.datetime.now().ctime()}')
    while run:
        schedule.exec_jobs()
        sleep(1)

    logger.debug('Расписание остановлено')


# TODO: сделать задание расписания через сообщение
def set_schedule(task: Callable, *, hour=10, minute=0, second=0, **kwargs):
    """Создаёт расписание и возвращает экземпляр класса Scheduler"""
    schedule = Scheduler()
    schedule.daily(dt.time(hour=hour, minute=minute, second=second), task, kwargs=kwargs)
    return schedule


#

def get_str_holidays():
    parser = HolyParser()
    all_events = parser.get_all()
    return dict_to_format_string(all_events)


def send_morning_message(chat_id):
    greetings = generate_greeting()
    holidays = get_str_holidays()

    send_message_to_group(greetings, chat_id)
    send_message_to_group(holidays, chat_id)


if __name__ == '__main__':
    logger.info('Start bot')
    bot.polling(none_stop=True)  # запуск с параметром "не останавливать работу"
    logger.info('Bot has been stopped')
