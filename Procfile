web: gunicorn --pythonpath relMan relMan.wsgi

main_worker: celery -A relMan worker --beat -l info