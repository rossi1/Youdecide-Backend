from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Following(models.Model):
    following_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Followers(models.Model):
    follower_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following_set')
    following = models.ForeignKey(User, related_name='follower_set')

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return u'%s follows %s' % (self.follower, self.following)