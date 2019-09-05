from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from polls.models import Poll
from django.db.models.signals import post_save



#import cloudinary


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_likes')
    like_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-like_date',)
        unique_together = ('poll', 'user')
        


class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookmarks')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_bookmarks')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.question

    class Meta:
        ordering = ('-created',)
        unique_together = ('poll', 'user')
       


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_share')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_share')
    share_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.question

    class Meta:
        ordering = ('-share_date',)
        unique_together = ('poll', 'user')

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place_of_work = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(max_length=1200, null=True, blank=True)
    #image = cloudinary.models.CloudinaryField('images', default='avatar/customer.png')
    # image = CloudinaryField(
    #     'image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")
 
    def get_user(self):
        return User.objects.get(id=self.user_id)

  


    def __str__(self):
        return 'user id {} of {}'.format(self.user, self.pk)


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


