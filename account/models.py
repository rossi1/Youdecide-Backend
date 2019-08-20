from django.db import models
# from django.conf import settings
# users/models.py
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

"""
class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
"""
