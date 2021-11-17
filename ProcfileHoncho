web: gunicorn --pythonpath relMan relMan.wsgi

celery: celery -A relMan worker -l info

celerybeat: celery -A relMan beat -l info