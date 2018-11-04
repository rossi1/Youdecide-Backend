from django.db import models
from django.contrib.auth.models import User
from account.models import CustomUser


# Create your models here.
class UserProfile(models.Model):
    # user = models.ForeignKey(User, unique=True, related_name='user', on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, related_name='user', on_delete=models.CASCADE)
    # follows = models.ManyToManyField('self', related_name='follows_set', symmetrical=False)
    # followers = models.ForeignKey()
    # followers = models.ManyToManyField(User, related_name='followers_set', symmetrical=False)

    user_from = models.ForeignKey(CustomUser, related_name='rel_from_set', on_delete=models.CASCADE)  # A ForeignKey for the user that creates the
    #  relationship
    user_to = models.ForeignKey(CustomUser, related_name='rel_to_set', on_delete=models.CASCADE)  # A ForeignKey for the user being followed
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)