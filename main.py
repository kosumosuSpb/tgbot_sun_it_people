import logging.config
import datetime as dt
from time import sleep
from threading import Thread
from typing import Callable
import re
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

# SERVICE VARIABLES
run = True
schedule = None
tasks_thread = None


# КОМАНДЫ

@bot.message_handler(commands=['start'], chat_types=["private", "group", "supergroup"])
def cmd_start(message: telebot.types.Message):
    """Обработчик команды /start"""
    logger.debug(f'Got command: {message.text}')
    task = schedule or set_schedule(send_morning_message, chat_id=message.chat.id)

    global run
    global tasks_thread

    if tasks_thread:
        logger.debug('Перезагрузка треда с расписанием')
        run = False
        while tasks_thread.is_alive():
            sleep(1)
        run = True

    logger.debug('Запуск треда с расписанием')
    tasks_thread = Thread(target=start_tasks, args=(task,), name='Periodically_tasks').start()
    # logger.info('Расписание запущено')
    bot.send_message(message.chat.id, 'Расписание запущено. '
                                      'Для получения списка команд введите /help')


@bot.message_handler(commands=['help'], chat_types=["private", "group", "supergroup"])
def cmd_help_message(message: telebot.types.Message):
    """Обработчик команды /help"""
    logger.debug(f'Got command: {message.text}')
    bot.send_message(message.chat.id, '☮️ /start - запуск расписания (по-умолчанию в 10:00:00)\n'
                                      '☮️ /stop - остановка расписания\n'
                                      '☮️ /holidays - вывести праздники прямо сейчас\n'
                                      '☮️ /stop_bot - остановка бота (права только у владельца)\n'
                                      '☮️ /set_schedule HH:MM:SS - установка нового расписания\n'
                                      '☮️ /help - это сообщение')


@bot.message_handler(commands=['stop'], chat_types=["group", "supergroup"], is_chat_admin=True)
def cmd_stop(message: telebot.types.Message):
    """Обработчик команды /stop"""
    logger.debug(f'Got command: {message.text}')
    global run
    run = False
    bot.send_message(message.chat.id, f'Расписание остановлено пользователем '
                                      f'{message.from_user.first_name} ({message.from_user.username})')
    logger.info(f'Расписание остановлено пользователем {message.from_user.first_name} (@{message.from_user.username})')


@bot.message_handler(commands=['stop'], chat_types=["private"])
def cmd_stop(message: telebot.types.Message):
    """Обработчик команды /stop"""
    logger.debug(f'Got command: {message.text}')
    global run
    run = False
    bot.send_message(message.chat.id, f'Расписание остановлено пользователем '
                                      f'{message.from_user.first_name} ({message.from_user.username})')
    logger.info(f'Расписание остановлено пользователем {message.from_user.first_name} (@{message.from_user.username})')


@bot.message_handler(commands=['stop_bot'], chat_types=["private", "group", "supergroup"], is_chat_admin=True)
def cmd_stop_bot(message: telebot.types.Message):
    """Обработчик команды /stop_bot"""
    logger.debug(f'Got command: {message.text}')

    # TODO: переделать на нормальный фильтр
    if message.from_user.username != 'kosumosu':
        bot.send_message(message.chat.id, 'Доступ запрещён')

    global run
    run = False
    bot.send_message(message.chat.id, 'Бот остановлен')
    bot.stop_bot()
    logger.info('Бот остановлен')


@bot.message_handler(commands=['holidays'], chat_types=["private", "group", "supergroup"])
def cmd_get_holidays(message: telebot.types.Message):
    """Обработчик команды /holidays"""
    logger.debug(f'Got command: {message.text}')
    send_morning_message(message.chat.id)


@bot.message_handler(commands=['set_schedule'], chat_types=["private", "group", "supergroup"], is_chat_admin=True)
def cmd_set_schedule(message: telebot.types.Message):
    """Обработчик команды /set_schedule"""
    logger.debug(f'Got command: {message.text}')

    try:
        hour, minute, second = map(int, re.findall('[0-9]{2}', message.text))
    except ValueError:
        bot.reply_to(message, 'Не верный формат времени! Должен быть: HH:MM:SS, например: 10:00:00')
        return

    logger.debug(f'Запущено изменение расписания. Новое время: {hour}:{minute}:{second}')
    global schedule
    schedule = set_schedule(send_morning_message, hour=hour, minute=minute, second=second)
    cmd_start(message)


# СОБЫТИЯ

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
    logger.debug(f'Left member: {member}')
    bot.send_message(message.chat.id, f"{member.first_name} (@{member.username}) покинул(а) чат о_О")


# TASKS

def start_tasks(schedule: Scheduler):
    logger.debug(f'Расписание запущено в {dt.datetime.now().ctime()}')
    logger.debug(schedule)
    while run:
        schedule.exec_jobs()
        sleep(1)
    logger.debug('Расписание остановлено')


# TODO: сделать задание расписания через сообщение
def set_schedule(task: Callable, *, hour=None, minute=None, second=None, **kwargs):
    """Создаёт расписание и возвращает экземпляр класса Scheduler"""
    schedule = Scheduler()
    hour = hour or HOUR
    minute = minute or MINUTE
    second = second or SECOND
    schedule.daily(dt.time(hour=hour, minute=minute, second=second), task, kwargs=kwargs)
    return schedule


#

def get_str_holidays():
    parser = HolyParser()
    all_events = parser.get_all()
    return dict_to_format_string(all_events)


def send_morning_message(chat_id, with_greetings=True):
    greetings = generate_greeting()
    holidays = get_str_holidays()

    if with_greetings:
        bot.send_message(chat_id, greetings)
    bot.send_message(chat_id, holidays)


if __name__ == '__main__':
    logger.info('Start bot')
    bot.polling(none_stop=True)
    logger.info('Bot has been stopped')
