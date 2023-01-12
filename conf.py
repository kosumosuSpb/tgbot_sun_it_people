TOKEN = ""  # токен, полученный при регистрации
HOLIDAYS_SOURCE = 'https://kakoysegodnyaprazdnik.ru/'
HOROSCOPE_SOURCE = ''

# CELERY CONFIG
celery_broker_url = 'redis://localhost:6379/0'
celery_result_backend = 'redis://localhost:6379/0'
# celery_broker_url = 'redis://redis:6379/0'
# celery_result_backend = 'redis://redis:6379/1'

celery_task_serializer = 'json'
celery_result_serializer = 'json'
celery_accept_content = ['json']
celery_timezone = 'Europe/Moscow'
celery_enable_utc = True
