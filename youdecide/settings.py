"""
Django settings for youdecide project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.urls import reverse_lazy
from decouple import config


LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# AUTH_USER_MODEL = 'account.CustomUser' # new to set the user auth to this

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '192.168.10.12']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'api',
    'pages',
    'polls',
    'home',
    'survey',
    'voting',
    'votes',
    'userprofile',
    'django_nose',
    #  'youdecide_frontend',
    'rest_framework.authtoken',
    'rest_framework',
    # social authentication
    # 'python-social-auth',
    'social_django',
    'tasks',
    'djcelery',

]
#
# AUTHENTICATION_BACKENDS = (
#                             'django.contrib.auth.backends.ModelBackend',
#                             # 'account.authentication.EmailAuthBackend',
#                                 'social.backends.facebook.Facebook2OAuth2',
#                             )
# SOCIAL_AUTH_FACEBOOK_KEY = 'XXX' # Facebook App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX' # Facebook App Secret

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST_FRAMEWORK = {
#                 'DEFAULT_PERMISSION_CLASSES': [
#                     # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#                 ]
#                 }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
ROOT_URLCONF = 'youdecide.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                # uncomment this to use vue template
                os.path.join(BASE_DIR, 'build'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'youdecide.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'NAME': 'YOUDECIDE',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': '1234567i0',
        'PORT': '5432',
        'HOST':'',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': config('DB_NAME'),
    #     'USER': config('DB_USER'),
    #     'PASSWORD': config('DB_PASSWORD'),
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # uncomment this to use vue static file
    os.path.join(BASE_DIR, 'build/static'),
]

# path for media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# uncomment this to use vue frontend
# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'build/static'),
# ]
