# sample/tasks.py
from __future__ import absolute_import
import requests
from celery import shared_task


# Define mailgun sending email API as a celery task
@shared_task(name="tsask.send_email")
def send_email(API_BASE_URL, API_KEY, CUSTOMER_LIST):
    return requests.post(
        API_BASE_URL,
        auth=("api", API_KEY),
        data={"from": "Developer contact@narenarya.in",
              "to": CUSTOMER_LIST,
              "subject": "Hello!",
              "text": "Thanks for signing up with us!."})