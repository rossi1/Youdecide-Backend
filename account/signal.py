from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from userprofile.models import Profile
from emailservice.utils import Mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_business_account_for_new_user(sender, created, instance, **kwargs):
    if created and instance:
        Profile.objects.create(user=instance)
            #"""
           # mail = Mail()
           # mail.add_receipent_to_contact_list(instance.email, instance.first_name, instance.last_name)
           # """