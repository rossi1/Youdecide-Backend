import json
import random

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from django_celery_beat.models import  PeriodicTask

from .utils import filter_votes, schedule_task

from tasks.tasks import mark_expired_polls


from .models import Poll


@receiver(post_save, sender=Poll)
def create_task(sender, created, instance, **kwargs):
    if created and instance:
        schedule  =  schedule_task(date=instance.expire_date)
        random_number  = random.randint(0, 99)
        name = 'Marking polls expired {}'.format(random_number)
        print(instance.id)
        #create_task(schedule, instance.)
        PeriodicTask.objects.create(
        clocked=schedule,
        name=name,
        task='tasks.tasks.mark_expired_polls',
        args=json.dumps((instance.id,)))
        