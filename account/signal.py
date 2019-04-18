from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from emailservice.utils import Mail



"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_business_account_for_new_user(sender, created, instance, **kwargs):
    if created:
        mail = Mail()
        mail.add_receipent_to_contact_list(instance.email)

"""