from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from polls.models import Poll
from django.db.models.signals import post_save
# from cloudinary.models import CloudinaryField


# Create your models here.
class UserProfile(models.Model):
    # user = models.ForeignKey(User, unique=True, related_name='user', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    # follows = models.ManyToManyField('self', related_name='follows_set', symmetrical=False)
    # followers = models.ForeignKey()
    # followers = models.ManyToManyField(User, related_name='followers_set', symmetrical=False)

    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    # A ForeignKey for the user that creates the relationship
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    # A ForeignKey for the user being followed
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.CharField(max_length=255)
    like_date = models.DateTimeField(auto_now_add=True)


class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.question

    class Meta:
        ordering = ('-created',)


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # poll = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    share_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.question

    class Meta:
        ordering = ('-share_date',)


class UserProfile2(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place_of_work = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(max_length=1200, null=True, blank=True)
    # image = CloudinaryField(
    #     'image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")

    def get_user(self):
        return User.objects.get(id=self.user_id)

    def get_followers(self):
        # return a list of users following this instance
        return self.user.follower.all()

    def get_following(self):
        # return a list of users followed by this instance
        return self.user.following.all()

    @property
    def followings(self):
        followers = self.user.follower.all()
        follow = []
        for follower in followers:
            follow.append(
                {'id': follower.followed.id,
                 'following': follower.followed.username,
                 'follow_date': follower.date_of_follow})
        return follow

    @property
    def followers(self):
        followings = self.user.following.all()
        follow = []
        for following in followings:
            follow.append(
                {'id': following.follower.id,
                 'follower': following.follower.username,
                 'follow_date': following.date_of_follow})
        return follow

    # @property
    # def languages(self):
    #     return [language for language in self.user.languages.all()]


# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
#
# post_save.connect(create_user_profile, sender=User)


class UserSettings(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='settings')
    # frequency = models.CharField(default="daily", null=True, max_length=10)

    # @property
    # def languages(self):
    #     return [language for language in self.user.languages.all()]


class Follow(models.Model):

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date_of_follow = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'followed'),)


# class Language(models.Model):
#
#     user = models.ForeignKey(User, related_name="languages")
#     name = models.CharField(max_length=200, null=True)
#
#     class Meta:
#         unique_together = (('user', 'name'),)
#
#     def __str__(self):
#         return self.name


# class Notification(models.Model):
#
#     user = models.ForeignKey(User, related_name="notifications")
#     link = models.CharField(max_length=200, null=True)
#     activity_type = models.CharField(max_length=50, null=False)
#     read = models.BooleanField()
#     content = models.TextField(max_length=1200, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.content
#
#     class Meta:
#         ordering = ['-date_created']
