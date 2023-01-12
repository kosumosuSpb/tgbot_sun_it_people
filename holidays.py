import requests
from bs4 import BeautifulSoup
import logging
#
from conf import HOLIDAYS_SOURCE


logger = logging.getLogger('HolidayParser')
logger.setLevel(logging.DEBUG)


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
            'holidays': holidays,
            'events': events
        }

    def get_page(self, source='') -> str:
        source = source or self.source
        html = requests.get(source, headers=self.headers)
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
