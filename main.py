import logging
from conf import TOKEN
import telebot
from time import sleep, localtime
from threading import Thread
#
from holidays import HolyParser
from utils import *

logger = logging.getLogger('Greetings_TGBot')
logger.setLevel(logging.DEBUG)
# TODO: добавить логи в файл

bot = telebot.TeleBot(TOKEN)  # создание экземпляра класса TeleBot и передача токена ему
run = True


@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start"""
    bot.send_message(message.chat.id, 'текст для вывода на команду /start')


@bot.message_handler(commands=['help'])
def help_message(message):
    """Обработчик команды /help"""
    bot.send_message(message.chat.id, 'тест для вывода на команду /help')


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    """Обработчик команды /stop"""
    # TODO: добавить проверку пользователя, который делает команду


    global run
    run = False
    bot.stop_bot()


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    """Приветствие вошедших пользователей"""
    name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, f"Добро пожаловать, @{name}!")


def send_message_to_group(message):
    """отправка сообщения в группу"""


def primitive_cron(interval=3, hours=10):
    """Просто каждую минуту сверяется с часами, в 10 утра запускает парсинг и отправку сообщения в группу"""
    logger.debug('Примитивный планировщик запущен')
    global run
    while run:
        sleep(interval)
        if localtime().tm_hour == hours:
            parser = HolyParser()
            all_events = parser.get_all()
            message = dict_to_format_string(all_events)
            send_message_to_group(message)


if __name__ == '__main__':
    try:
        Thread(target=primitive_cron, name='Primitive_cron').start()
        bot.polling(none_stop=True)  # запуск с параметром "не останавливать работу"
    except KeyboardInterrupt:
        run = False
        bot.stop_bot()
        print('Остановлено пользователем')
