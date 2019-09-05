# # sample/tasks.py
# from __future__ import absolute_import
# import requests
# from celery import shared_task
#
#
# # Define mailgun sending email API as a celery task
# @shared_task(name="tsask.send_email")
# def send_email(API_BASE_URL, API_KEY, CUSTOMER_LIST):
#     return requests.post(
#         API_BASE_URL,
#         auth=("api", API_KEY),
#         data={"from": "Developer contact@narenarya.in",
#               "to": CUSTOMER_LIST,
#               "subject": "Hello!",
#               "text": "Thanks for signing up with us!."})

import json
from datetime import timedelta, datetime

from django.conf import settings
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder

from celery import shared_task
from celery.schedules import crontab

from celery.decorators import periodic_task

from polls.models import Poll


@shared_task
def send_registration_welcome_mail(email, username):
    subject = "Youdecide Registration Message"
    message_body = "Hello {}, welcome to youdecide polling system".format(username)
    mail_user = send_mail(subject, message_body, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    return mail_user


@periodic_task(
    run_every=(crontab('*/1')),
    name='task_update_polls',
    ignore_result=True
)
def mark_expired_polls():
    for polls in Poll.objects.all():
        if polls.expire_date is None:
            pass
        elif polls.expire_date == datetime.today():
                polls.has_expired = True
                return polls.save()

