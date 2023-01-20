# Telegram Bot for sun_it_people chat

_На ранней стадии_

## Что умеет/~~будет уметь~~:

* Приветствовать входящих в чат
* Оповещать, когда кто-то уходит
* По расписанию желает доброго утра, показывает, какой сегодня праздник и какие события происходили в прошлом. Берётся из сайта [https://kakoysegodnyaprazdnik.ru](https://kakoysegodnyaprazdnik.ru) и парсер приспособлен только на него.
* Админы чата могут настраивать расписание через сообщения
* Можно вызвать показ сегодняшних праздников

## Команды

* `/start` - запуск расписания (по-умолчанию в 10:00:00)
* `/stop` - остановка расписания
* `/holidays` - вывести праздники прямо сейчас
* `/stop_bot` - остановка бота (права только у владельца)
* `/set_schedule` HH:MM:SS - установка нового расписания
* `/help` - выводит список команд
