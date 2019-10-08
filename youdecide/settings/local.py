from youdecide.settings.base import *
from decouple import config


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
"""
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
"""


DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'youdecide',
         'USER': 'postgres',
         'PASSWORD': 'emma',
         'HOST': '',
         'PORT': '5432',
         }
}

CELERY_LOCALHOST = "redis://h:p6e1f8caec4db141af95effe7fa212d2a658f1655fa14e84fe2102b8a00ba771e@ec2-34-206-10-16.compute-1.amazonaws.com:28149"

BROKEN_URL = CELERY_LOCALHOST
CELERY_BROKER_URL = CELERY_LOCALHOST
CELERY_RESULT_BACKEND = CELERY_LOCALHOST
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Lagos'
 

"""
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
"""

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': config('BONSAI_URL')
    },
}
