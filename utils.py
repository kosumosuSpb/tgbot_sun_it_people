import logging.config
#
from conf import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('Utils')


def dict_to_format_string(dct: dict) -> str:
    """Переводит словарь в строку, которую можно отправить в виде сообщения"""
    res = ''
    for key, val in dct.items():
        res += key + '\n\n' + '\n'.join(['• ' + day for day in val]) + '\n\n'

    return res
