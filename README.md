# Youdecide

## Description
Youdecide is a Social Network polling platform.


## Installation
1. Clone the repository and create a Virtual Environment.
    - Run `virtualenv <virtualenvname>` to create the virtual environment or `mkvirtualenv <virtualenvname>` if using virtualenv wrapper to create the virtual environment.
2. Install all the necessary requirements by running `pip install -r requirements.txt` within the virtual environment.
3. Configure your database configurations in a *development.py* and save in the settings folder (sample shown below)
You'll need to install postgres for this. If you don't have it installed, download it [here](https://www.postgresql.org/download/).
    ##### Sample development.py
    ```
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    from .base import *
    import sys

    if 'test' in sys.argv:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'testdatabase',
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'youdecide', # Enter your database's name
                'USER': 'user', # Enter your DB user
                'PASSWORD': 'p@ssw0rd', # Enter your DB password
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
    ```
    If you prefer another 3rd party DB backend update the second `'ENGINE'` value accordingly
4. Create a *.env.yml* to hold all your environment variables, like your secret key, save in the same level as your README.md file (sample shown below)
    ##### Sample .env.yml format
    ```
    api_key:
    "123456789101112"  # This is your API key
    api_secret:
    "Abc_DefgHIjKlmn-O1pqRStu2V"  # This is your API secret
    cloud_name:
    "youdecidefile"
    SECRET_KEY:
    "12345678910111213141516171819202122232425"  # This is the Secret key
    sendgrid_apikey:
    "1234567891011121314151617181920212223242526272829303132333435"  # This is your SendGrid API Key
    GITHUB_CLIENT_ID:
        "123456789101112131415"  # This is your Github client ID
    GITHUB_SECRET_KEY:
        "12345678910111213141516171819202122232425"  # This is your Github secret Key
    CELERY_NOTIFICATION_TIMEOUT:
        "10"  # This is the timeout set to 10 seconds (Increase this parameter for production)

    ```
5. Run `npm install` to install all front end dependencies. Please ensure you are on the same level with .bowerrc when you run this command
6. Run `cd youdecide` to navigate into the project directory
7. Run `python manage.py collectstatic` to copy all your static files into the staticfiles directory
8. Run `python manage.py makemigrations` and `python manage.py migrate` to create the necessary tables and everything required to run the application.
9. Run `python manage.py runserver` to run the app.
10. Run `coverage run manage.py test` to know how much the app is covered by automated testing.
11. Run `coverage report` to view the report of the coverage on your terminal.
12. Run `coverage html` to produce the html of coverage result.

## Running tests
1. Activate virtual environment.
2. Navigate into the project directory.
3. Run `python manage.py test` to test codango.
4. Run `python manage.py test <appname>` to test an individual app.
5. Run `coverage run manage.py test` to run coverage for codango.

## REST API
Youdecide has a REpresentational State Transfer (REST) Application Program Interface (API)
The documentation done on Apiary is [here](http://docs.youdecide.apiary.io/).

The API endpoints are accessible at [localhost:8000/api/v1/](http://localhost:8000/api/v1/)

To run tests specific to the API Run `python manage.py test api`
pip install mysqlclient

pip install pymysql
Then, edit the __init__.py file in your project origin dir(the same as settings.py)

add:

import pymysql

pymysql.install_as_MySQLdb()

## run app
edit wsgi.py os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youdecide.settings.SPECIFIC_SETTINGS_NAME")
eg os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youdecide.settings.local")
python manage.py runserver --settings=youdecide.settings.['local' or 'production' or 'test' etc]


## Copyright
Youdecide © 2015 - 2016 YOUDECIDE

### Install ngrok
run the command below for testing with different machines
ngrok http 8080 -host-header="localhost:8080"

