from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import F
from .models import VoteCount, Vote


@receiver(post_save, sender=Vote)
def update_polls_vote_count(sender, created, instance, **kwargs):
    if created:
        try:
            VoteCount.objects.get(poll_vote=instance.poll)
        except VoteCount.DoesNotExist:
            VoteCount.objects.create(poll_vote=instance.poll, vote_count = 1)
        else:
            VoteCount.objects.filter(poll_vote=instance.poll).update(vote_count=F('vote_count') + 1)
