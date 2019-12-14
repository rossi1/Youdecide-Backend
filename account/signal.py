from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from userprofile.models import Profile
from emailservice.utils import Mail


@receiver(post_save, sender=User)
def create_profile_account_for_new_user(sender, created, instance, **kwargs):
    if created and instance:
        Profile.objects.create(user=instance)
         