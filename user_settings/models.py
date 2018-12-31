from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Language(models.Model):

    user = models.ForeignKey(User, related_name="languages")
    name = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('user', 'name'),)

    def __str__(self):
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(User, related_name="notifications")
    link = models.CharField(max_length=200, null=True)
    activity_type = models.CharField(max_length=50, null=False)
    read = models.BooleanField()
    content = models.TextField(max_length=1200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date_created']