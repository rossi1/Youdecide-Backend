import nexmo
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
from decouple import config

FROM = 'Youdecide'
NEXMO_API_KEY = config('NEXMO_API_KEY')
NEXMO_API_SECRET = config('NEXMO_API_SECRET')
client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
recepient = '447415243436'
recepient2 = '2347038816743'
recepient3 = '2348032966542'
recepient4 = '2347065587424'
recepient5 = '2347032341059'
recepient6 = '2347088800781'
message = 'You have job from our anykillz client abbah'
message2 = 'Itsannie WE make the best designs of clothes in Africa for Africans by an African'
message3 = 'open account with Eme for best banking experience with Standbic'
message4 = 'Vote your best candidate 1. PMB  2. ATIKU'


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


@method_decorator(csrf_exempt, name='get')
class UserCreateSMS(APIView):
    """For /api/v1/sms/poll url path"""
    # authentication_classes = ()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = ()

    def get(self, request, message2s=None):
        sendSMS(recepient6, message4)
        return Response("success", status=status.HTTP_200_OK)


def sendSMS(to_recipient, text):
    client.send_message({
        'from': FROM,
        'to': to_recipient,
        'text': text,
    })
    
    
def sms_poll():
    """api/v1/sms/poll sends a specific poll with id as sms"""
    pass


def sms_vote():
    """api/v1/sms/poll-vote get user vote of a poll"""
    pass


def sms_reminder():
    """api/v1/sms/user_id"""
    pass


def sms_appointment_reminder():
    """api/v1/sms/appointment_id"""
    pass


def sms_notification():
    pass


def sms_verification():
    pass

    
def verify_phone_number():
    pass
    
    
def validate_phone_number(phone_number, country):
    pass
