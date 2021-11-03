from __future__ import absolute_import, unicode_literals
from datetime import timezone
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relMan.settings')

app = Celery('relMan')
app.conf.enable_utc = False

app.conf.update(timezone='America/Vancouver')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
