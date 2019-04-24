import requests 
import json

from django.conf import settings
from django.core.mail import send_mail




class Mail:
    headers = {
    "authorization": "Bearer {}".format(settings.SENDGRID_API_KEY),
    "content-type": "application/json"
    }

    contact_api_url = "https://api.sendgrid.com/v3/contactdb/recipients"

    def add_receipent_to_contact_list(self, email_payload, first_name, last_name):
        """This method is used to subscribe users to mailing lists """
        data = [{'email': email_payload, 'first_name':first_name,  'last_name': last_name}]
        
        return requests.post(self.contact_api_url, json=data, headers=self.headers)

    def send_welcome_mail(self, email, username):
        subject = "Youdecide Registration Message"
        message_body = "Hello {}, welcome to youdecide polling system".format(username) #this is an unstructured email body

        mail_user = send_mail(subject, message_body, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return mail_user

    