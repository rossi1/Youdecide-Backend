
from youdecide.settings.base import *


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {}

DATABASES['default'] =  dj_database_url.config(default=config('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql',



ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}



