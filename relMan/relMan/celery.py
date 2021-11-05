from __future__ import absolute_import, unicode_literals
from datetime import timezone
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relMan.settings')

app = Celery('relMan')
app.conf.enable_utc = False

app.conf.update(timezone='America/Vancouver')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-2days': {
        'task': 'dates.tasks.two_days_prior',
        'schedule': crontab(hour=0, minute=1),
    },
    'send-mail-7days': {
        'task': 'dates.tasks.week_prior',
        'schedule': crontab(hour=0, minute=2),
    },
    'send-mail-30days': {
        'task': 'dates.tasks.month_prior',
        'schedule': crontab(hour=0, minute=3),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
