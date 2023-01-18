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

# GREETINGS
# TODO: вынести это в отдельные файлы в папке conf, например, и парсить при запуске
WHAT = ['Доброе утро', ]

WHICH = ['аппетитные', 'божественные', 'блестящие', 'благоуханные', 'бесценные', 'будоражащие', 'блистательные',
         'бесподобные', 'великолепные', 'великие', 'волнительные', 'воздушные', 'властные', 'вдохновляющие',
         'восхитительные', 'горячие', 'грациозные', 'дорогие', 'дивные', 'дражайшие', 'дикие', 'драгоценные',
         'дикие', 'единственные', 'желанные', 'женственные', 'золотые', 'загадочные', 'изумительные', 'идеальные',
         'креативные', 'красивые', 'лучезарные', 'ласковые', 'любимые', 'милые', 'маленькие', 'нежные', 'небесные',
         'ненаглядные', 'неповторимые', 'неотразимые', 'незабвенные', 'невероятные', 'неземные', 'обожаемые',
         'окрыляющие', 'очаровательные', 'обворожительные', 'привлекательные', 'пленительные', 'родные', 'сладкие',
         'сногсшибательные', 'сказочные', 'снежные', 'удивительные', 'фантастические', 'феерические', 'хорошие',
         'шикарные', 'яхонтовые']
WHO = ['антилопы', 'амурчики', 'ананасики', 'апельсинки', 'афродиты', 'аистенки', 'ангелы', 'ангелочки', 'бусеньки',
       'богини', 'бурундучки', 'барбариски', 'булочки', 'былинки', 'бельчонки', 'белочки', 'бриллиантики', 'бабочки',
       'бублички', 'бестии', 'бусинки', 'вредины', 'вафельки', 'волшебницы', 'вишенки', 'вкусняшки', 'виноградинки',
       'веснушки', 'ватрушечки', 'василки', 'голубки', 'горошинки', 'галчонки', 'гусенки', 'дорогуши', 'дюймовочки',
       'душечки', 'детки', 'души', 'мои', 'дельфиненки', 'дикобразики', 'ежики', 'ежиньки', 'егозы', 'ежевички',
       'жучки', 'жемчужины', 'золотца', 'забавы', 'зефирки', 'златовласки', 'звездочки', 'зайки', 'зайчики', 'зайчонки',
       'зайчоныши', 'звеpеныши', 'землянички', 'изумрудики', 'искусительницы', 'искорки', 'ириски', 'игрульки',
       'изюминки', 'киски', 'кошечки', 'котенки', 'кисульки', 'красотульки', 'козочки', 'колобки', 'капризульки',
       'карапузики', 'козявочки', 'кнопки', 'котлетки', 'кнопочки', 'крохотульки', 'колючки', 'крокозябрики',
       'карасики', 'красотки', 'кошечки', 'кукушонки', 'круассанчики', 'куксики', 'кровиночки', 'кролики', 'кролички',
       'крошки', 'конфетки', 'клубнички', 'клюковки', 'карамельки', 'красавицы', 'курочки', 'куколки', 'кудряшки',
       'кускусики', 'лютики', 'лебедушки', 'лапочки', 'лучики', 'лапушки', 'лапули', 'ляли', 'лялечки', 'лапки',
       'львенки', 'лимпопоши', 'лепесточки', 'ласточки', 'льдинки', 'лимончики', 'лисенки', 'лани', 'ласкуши',
       'ласточки', 'лягушонки', 'малыши', 'малышки', 'мурлыки', 'малютки', 'малявочки', 'мальвинки', 'мармеладки',
       'медвежонки', 'малышки', 'мурзеныши', 'мяфмяфочки', 'мисюси', 'мушки', 'мечты', 'морковки', 'мумитролльчики',
       'малинки', 'мусики', 'мурзилки', 'мышонки', 'мимишечки', 'незабудки', 'няши', 'нямочки', 'обаяшки', 'очаровашки',
       'осинки', 'облачки', 'олененки', 'одуванчики', 'обольстительницы', 'огонки', 'персики', 'птенчики', 'пташки',
       'пушинки', 'поросеночки', 'пупсики', 'пупсеныши', 'печеньки', 'проказницы', 'прелести', 'пельмешки', 'плюшечки',
       'пампушечки', 'пончики', 'поночки', 'перчики', 'пусики', 'пятачки', 'пингвинчики', 'пузатики', 'полосатики',
       'паровозики', 'половинки', 'пушистики', 'пушки', 'пpелестницы', 'пампушечки', 'пухляши', 'пухлики', 'розочки',
       'ромашки', 'рыбки', 'рыжики', 'рыжечки', 'рыжульки', 'радости', 'роднульки', 'рысенки', 'солнышки', 'сердечки',
       'сердцеедки', 'слапопуськи', 'слоненки', 'синички', 'соблазнительницы', 'сахарки', 'снежки', 'светлячки',
       'совенки', 'симпатяжки', 'смородинки', 'снежинки', 'снегирки', 'снежки', 'сокровища', 'тигренки', 'тигрульки',
       'тыковки', 'телепузики', 'тростинки', 'тефтельки', 'услады', 'усипуськи', 'ушастики', 'умницы', 'утенки', 'умки',
       'фунтики', 'финтифлюшки', 'хитрюгы', 'хомячки', 'херувимчики', 'цветочки', 'цветик-семицветики', 'цыпленки',
       'чуди', 'чебурашки', 'чеpтенки', 'черешенки', 'шалунишки', 'шоколадки', 'щекастики', 'эклерчики', 'ягодки',
       'ясноглазки', 'яблочки', 'пушистики']

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
        'GreeTG_Bot': {
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
