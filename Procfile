web: gunicorn youdecide.wsgi
worker: celery -A tasks worker --loglevel=info
beat: celery -A tasks beat -l info -S django