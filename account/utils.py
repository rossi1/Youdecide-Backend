import jwt
from datetime import timedelta, datetime

from django.conf import settings

def encode_user_payload(user):
        if isinstance(user, str):
                payload = {'user': user , 'exp': datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_DELTA_MINTUES)}
        else:
                payload = { 'user': user.email , 'exp': datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_DELTA_MINTUES)}
        jwt_token = jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        return jwt_token.decode('utf-8')

