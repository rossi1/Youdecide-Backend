
from youdecide.settings.base import *


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {}

DATABASES['default'] =  dj_database_url.config(default=config('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql',



ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'https://g47gae624z:t3oy2k6ze2@jasmine-116574974.us-east-1.bonsaisearch.net:443'
    },
}







