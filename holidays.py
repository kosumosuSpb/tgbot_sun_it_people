import requests
from bs4 import BeautifulSoup
import logging.config
#
from conf import HOLIDAYS_SOURCE, LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('HolidayParser')


class HolyParser:
    """
    Парсер праздников, заточен под 'https://kakoysegodnyaprazdnik.ru/'

    parser = HolyParser()
    days = parser.get_all()

    В итоге будет словарь:
    {
        'holidays': [ ... ],
        'events': [ ... ]
    }
    """
    def __init__(self, source=None):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.source = source or HOLIDAYS_SOURCE
        
    def get_all(self) -> dict:
        """Вернёт события и праздники в словаре"""
        page = self.get_page(self.source)
        holidays = self.get_holidays(page)
        events = self.get_events(page)
        return {
            'Праздник': holidays,
            'События в истории': events
        }

    def get_page(self, source='') -> str:
        source = source or self.source
        logger.debug(f'Запрос страницы {source}')
        html = requests.get(source, headers=self.headers)
        logger.debug(f'Ответный код: {html.status_code}')
        html.encoding = 'utf-8'  # сайт выдаёт криво кодировку почему-то, так что исправляем
        return html.text

    @staticmethod
    def get_holidays(page: str) -> list:
        soup = BeautifulSoup(page, 'html.parser')
        return [day.text for day in soup.find_all(itemprop='text')]

    @staticmethod
    def get_events(page: str) -> list:
        soup = BeautifulSoup(page, 'html.parser')
        # находим все div с классом event,
        # возвращаем список событий, попутно убирая точку впереди и текст с тем, сколько лет назад это было
        return [day.text.replace('• ', '').replace(day.span.text, '') for day in soup.find_all('div', class_='event')]
