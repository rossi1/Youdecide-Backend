from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='user')
    follows = models.ManyToManyField('self', related_name='follows_set', symmetrical=False)
    # followers = models.ForeignKey()
    followers = models.ManyToManyField(User, related_name='followers_set', symmetrical=False)