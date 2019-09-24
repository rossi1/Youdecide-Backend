from youdecide.settings.base import *


DATABASES = {}

DATABASES['default'] =  dj_database_url.config(default=config('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql',


DEBUG = True

# Elasticsearch configuration
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': config('BONSAI_URL')
    },
}
