import logging.config
from random import choice
#
from conf import *


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('Utils')


def dict_to_format_string(dct: dict) -> str:
    """Переводит словарь в строку, которую можно отправить в виде сообщения"""
    res = ''
    for key, val in dct.items():
        res += key + '\n\n' + '\n'.join(['• ' + day for day in val]) + '\n\n'

    return res


def generate_greeting():
    """Генерирует приветствие из возможных вариантов, прописанных в конфиге"""
    what = choice(WHAT)
    which = choice(WHICH)
    who = choice(WHO)
    return f'{what}, {which} {who}!'

