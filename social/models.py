from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from polls.models import Poll
from userprofile.models import  Likes


class FollowQuerySet(models.query.QuerySet):
    """Personalized queryset created to improve model usability."""

    def get_followers(self, user):
        followers = self.filter(following=user).order_by('-date_follow').all()
        total_followers_no = self.filter(following=user).all().count()
        follow = [{'total_followers_no': total_followers_no}]
        for follower in followers:
            follow.append(
                
                {'id': follower.pk,
                 'follwer_id': follower.follower.id,
                 'follower_username': follower.follower.username,
                 'follow_date': follower.date_follow
                }
                )
        return follow

    def get_followings(self, user):
        followings = self.filter(follower=user).order_by('-date_follow').all()
        total_followers_no = self.filter(follower=user).all().count()
        follow = [{'total_followed_no': total_followers_no}]
        for following in followings:
            follow.append(
                {'id': following.pk,
                 'following_id': following.following.id,
                 'following_username': following.following.username,
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

