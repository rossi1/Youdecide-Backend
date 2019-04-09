from django.db import models


# Create your models here.
# to detect and ignore "duplicate" votes instead(i.e.votes for the same
# option from the same ip and browser combination for certain time period may be considered "cheated").
class AnonymousUserModel(models.Model):
    user_ip = models.GenericIPAddressField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.user_ip)


class AnonymousVoter(models.Model):
    # anonymous_voter_id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=16)
    email_address = models.CharField(unique=True, max_length=255, blank=True, null=True)
    useragent = models.TextField(blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(max_length=60, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(max_length=60, blank=True, null=True)
    ip_address = models.CharField(max_length=40, blank=True, null=True)
    browsername = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    browserversion = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField()

   

