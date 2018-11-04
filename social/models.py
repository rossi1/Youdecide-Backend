from django.db import models
from django.contrib.auth.models import User
from account.models import CustomUser


# Create your models here.
class Following(models.Model):
    following_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Followers(models.Model):
    follower_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class MyPolls(models.Model):
    pass


class Follower(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following_set')
    following = models.ForeignKey(CustomUser, related_name='follower_set')

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return u'%s follows %s' % (self.follower, self.following)