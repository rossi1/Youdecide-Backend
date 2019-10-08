
from rest_framework.authentication import SessionAuthentication


import jwt

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, \
    get_authorization_header



try:
    from django.urls import reverse
except ImportError:  # Will be removed in Django 2.0
    from django.core.urlresolvers import reverse

from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions, HTTP_HEADER_ENCODING

from social_django.views import NAMESPACE
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend
from social_core.utils import requests




class JwtAuthentication(authentication.BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        token = get_authorization_header(request).split()

        if not token or token[0].lower() != self.keyword.lower().encode():
            return None

        if len(token) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(token) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        else: 
            try:
                user = jwt.decode(token[1].decode(), settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)
            
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed({
                    'message': 'false',
                    'res': False,
                    'reason': 'Token expired'})
            
            except jwt.DecodeError:
                raise exceptions.AuthenticationFailed({
                    'message': 'false',
                    'res': False,
                    'reason': 'Invalid Token'})

            else:
                user_ = get_user_model().objects.get(email__iexact=user['user'])
                return (user_, token)

    def authenticate_header(self, request):
        return self.keyword

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


    