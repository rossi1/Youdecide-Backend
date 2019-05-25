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

import dj_database_url


#LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
#LOGIN_URL = reverse_lazy('login')
#LOGOUT_URL = reverse_lazy('logout')

# AUTH_USER_MODEL = 'account.CustomUser' # new to set the user auth to this

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


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
    'anonymous_user',
    # 'pages',
    'polls',
    'home',
    'survey',
    'sms',
    'voting',
    'votes',
    'userprofile',
    'django_nose',
    'search',
    #  'youdecide_frontend',
    'rest_framework.authtoken',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    # social authentication
    # 'python-social-auth',
    'social_django',
    'corsheaders',
    'oauth2_provider',
    'rest_framework_social_oauth2'
    

    #  'tasks',
    #  'djcelery',

]

# authentication backends
# user can login with username or email as username
AUTHENTICATION_BACKENDS = (
    # 'django.contrib.auth.backends.ModelBackend', # for django 1.8.3
    'django.contrib.auth.backends.AllowAllUsersModelBackend', # for django 1.10 to test is_active user
    'account.customauthbackend.EmailOrUsernameModelBackend',
    # facebook auth backend
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

     # Google OAuth2
    # 'social.backends.google.GoogleOAuth2',
    
     # Twitter Oauth
    'social_core.backends.twitter.TwitterOAuth',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',


)
SOCIAL_AUTH_FACEBOOK_KEY = config('FACEBOOK_APP_ID') # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = config('FACEBOOK_APP_SECRET') # Facebook App Secret


# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_SECRET_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email',]

# SOCIAL_AUTH_TWITTER_KEY = config('TWITER_KEY')
# SOCIAL_AUTH_TWITTER_SECRET = config('TWITTER_SECRET_KEY')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# enable CORS for all domains
CORS_ORIGIN_ALLOW_ALL = True


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
                 # OAuth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'youdecide.wsgi.application'


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
