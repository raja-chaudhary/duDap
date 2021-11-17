web: gunicorn --pythonpath relMan relMan.wsgi

celery: celery -A relMan worker -l info

beat: celery -A relMan beat -l info