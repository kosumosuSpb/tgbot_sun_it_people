from celery import Celery
from celery.schedules import crontab


app = Celery('tgbot')
app.config_from_object('conf', namespace='celery')  # conf - имя файла с конфигом, namespace - префикс переменных
# запуск воркера будет такой:
# celery -A celery_app worker -l INFO
# запуск периодических задач:
# celery -A celery_app beat -l INFO

# настройка расписания (когда будет рассылка уведомлений происходить)
# при желании можно сделать так, чтобы клиент мог сам настраивать, когда ему будет приходить рассылка,
# но это усложнило бы всю схему, т.к. нужно прикручивать динамическое создание периодических тасков
# https://docs.celeryq.dev/en/master/userguide/periodic-tasks.html
app.conf.beat_schedule = {
    # Executes every day 10:00 a.m.
    'add-every-day-morning': {
        'task': 'celery_app.start_daily_reminder',
        'schedule': crontab(hour=10, minute=0),
        # 'args': (),
    },
    # 'test-every-5-seconds': {
    #     'task': 'celery_app.test_task',
    #     'schedule': 5.0,
    #     'args': (16, 16)
    # },
}


@app.task
def test_task(*args, **kwargs):
    """Тестовая задача"""
    print('Test task ran success')


app.autodiscover_tasks()
