from youdecide.settings.base import *
from decouple import config


REST_FRAMEWORK = {

                'DEFAULT_PERMISSION_CLASSES': [
                    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
                ]
            }

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
         'ENGINE': config('DB_POSTGRES_ENGINE'),
         'NAME': config('DB_NAME'),
         'USER': config('DB_USER'),
         'PASSWORD': config('DB_PASSWORD'),
         'HOST': '',
         'PORT': '5432',
 }

}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8080'
    '192.168.10.13:8080'
    '*'
)