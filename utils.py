import logging.config
#
from conf import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('Utils')


def dict_to_format_string(dct: dict) -> str:
    """Переводит словарь в строку, которую можно отправить в виде сообщения"""
    for key, val in dct.items():
        pass
    return str()
