# from __future__ import absolute_import
#
# import os
#
# from celery import Celery
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youdecide.settings')
#
# from django.conf import settings  # noqa
#
# app = Celery('tasks')
#
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


import os

from django.conf import settings

from celery import Celery


from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youdecide.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('tasks', broker='redis://h:p6e1f8caec4db141af95effe7fa212d2a658f1655fa14e84fe2102b8a00ba771e@ec2-34-206-10-16.compute-1.amazonaws.com:28149')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)