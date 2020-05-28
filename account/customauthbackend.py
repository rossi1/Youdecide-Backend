from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import validate_email


class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
    
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(User.USERNAME_FIELD)
            user = User._default_manager.get(**{case_insensitive_username_field: username})
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User.set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


class EmailOrUsernameModelBackend(object):

    def authenticate(self, username=None, password=None):
        if self.validateEmail(username):
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def validateEmail(self, email):
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
