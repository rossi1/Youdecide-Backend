from youdecide.settings.base import *
from decouple import config


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': config('DB_POSTGRES_ENGINE'),
         'NAME': config('DB_NAME'),
         'USER': config('DB_USER'),
         'PASSWORD': config('DB_PASSWORD'),
         'HOST': '',
         'PORT': '5432',
         }
}

CELERY_LOCALHOST = 'redis://localhost:6379'
BROKEN_URL = CELERY_LOCALHOST
CELERY_RESULT_BACKEND = CELERY_LOCALHOST
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Lagos'
