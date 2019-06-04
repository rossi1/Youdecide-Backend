from datetime import timedelta
from youdecide.settings.base import *


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',  # enables simple command line authentication
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        #'rest_framework.permissions.IsAuthenticated',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # testing
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # testing
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': config('SECRET_KEY'),
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    
}


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

"""
DATABASES = {}

DATABASES['default'] =  dj_database_url.config(default=config('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql',
"""
# Email


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('HOST_USER')
EMAIL_HOST_PASSWORD = config('HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# sendgrid

SENDGRID_API_KEY=config('SENDGRID_API_KEY')
