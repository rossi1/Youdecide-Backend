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

   

