from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','hacker_news.settings')

app = Celery('hacker_news')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "fetch latest news": {
        "task": "news.tasks.get_latest_news",
        "schedule": crontab(minute="*/20")
    },
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')


































"""
from celery.schedules import crontab
app.conf.beat_schedule = {
    'multiply-task-crontab': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
    'multiply-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'movies.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
"""