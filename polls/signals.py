from django.dispatch import receiver
from django.db.models.signals import post_save


from userprofile.models import Profile
from emailservice.utils import Mail
from social.models import Follow
from notification.models import Notification

from .models import Poll
@receiver(post_save, sender=Poll)
def create_profile_account_for_new_user(sender, created, instance, **kwargs):
    if created:
        poll_viewers = Follow.objects.get_followers_list(instance.created_by)
        verb = "{} created a new poll".format(instance.created_by.username)
        notification = Notification.objects.create()

       