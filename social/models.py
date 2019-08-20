from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from polls.models import Poll
from userprofile.models import Share, Likes


class FollowQuerySet(models.query.QuerySet):
    """Personalized queryset created to improve model usability."""

    def validate_follow(self, follower):
        query = self.filter(follower=follower, following=follower)
        return False

    def get_followers(self, user):
        followers = self.filter(following=user).order_by('-date_follow').all()
        total_followers_no = self.filter(following=user).all().count()
        follow = [{'total_followers_no': total_followers_no}]
        for follower in followers:
            follow.append(
                {'id': follower.follower.id,
                 'follower': follower.follower.username,
                 'follow_date': follower.date_follow}
                 )
        return follow

    def get_followings(self, user):
        followings = self.filter(follower=user).order_by('-date_follow').all()
        total_followers_no = self.filter(follower=user).all().count()
        follow = [{'total_followed_no': total_followers_no}]
        for following in followings:
            follow.append(
                {'id': following.following.id,
                 'following': following.following.username,
                 'following_date': following.date_follow}
                 )
        return follow

    def get_followers_list(self, user):
        followers = self.filter(following=user).order_by('-date_follow').all()
        return [follower.follower.pk for follower in followers]

    def get_followings_list(self, user):
        followings = self.filter(follower=user).order_by('-date_follow').all()
        return [following.following.pk for following in followings]
     

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following')
    date_follow = models.DateTimeField(auto_now_add=True)
    objects = FollowQuerySet.as_manager()


    def __str__(self):
        return u'%s follows %s' % (self.follower, self.following)


"""
class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='follower_set', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return u'%s follows %s' % (self.follower, self.following)
"""