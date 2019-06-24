
from youdecide.settings.base import *




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




