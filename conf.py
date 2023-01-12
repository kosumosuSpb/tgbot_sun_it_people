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

# LOGGER CONFIG
STREAM_HANDLER_LEVEL = 'DEBUG'
FILE_HANDLER_LEVEL = 'DEBUG'
ERROR_FILE_HANDLER_LEVEL = 'ERROR'

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    # Loggers format
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        # 'short_formatter': {
        #     'format': '[%(levelname)-.1s] %(asctime)s (%(name)s) - %(message)s',
        #     'datefmt': '%H:%M:%S,%03d'
        # },
    },

    # Handlers
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
            'level': STREAM_HANDLER_LEVEL,
        },
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default_formatter',
            'level': FILE_HANDLER_LEVEL,
            'filename': './log/debug.log',
            'maxBytes': 51200,
            'backupCount': 5
        },
        'errors_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default_formatter',
            'level': ERROR_FILE_HANDLER_LEVEL,
            'filename': './log/errors.log',
            'maxBytes': 51200,
            'backupCount': 3
        }
    },

    # Loggers
    'loggers': {
        # '': {
        #     'handlers': ['stream_handler', 'file_handler', 'errors_file_handler'],
        #     'level': 'WARNING',
        #     'propagate': True
        # },
        'Greetings_TGBot': {
            'handlers': ['stream_handler', 'file_handler', 'errors_file_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'HolidayParser': {
            'handlers': ['stream_handler', 'file_handler', 'errors_file_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'Utils': {
            'handlers': ['stream_handler', 'file_handler', 'errors_file_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
