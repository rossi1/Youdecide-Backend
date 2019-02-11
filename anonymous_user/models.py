from django.db import models
from django.contrib.auth.models import AnonymousUser


# Create your models here.
# to detect and ignore "duplicate" votes instead(i.e.votes for the same
# option from the same ip and browser combination for certain time period may be considered "cheated").
class AnonymousUserModel(models.Model):
    user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=50)
    user_browser = models.CharField(max_length=100)
    user_ip = models.CharField(max_length=100)
    user_timezone = models.CharField(max_length=100)

