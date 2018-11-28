from django.db import models
from django.conf import settings
# users/models.py
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


# class CustomUser(AbstractUser):
#     # add additional fields in here
#     pass


class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class CustomUser(models.Model):
    users_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=225)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    # usertypeid = models.ForeignKey(UserType, models.DO_NOTHING, db_column='usertypeid')
    userstatus = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customusers'
