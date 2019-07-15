from django.db import models
from django.contrib.auth.models import User

from anonymous_user.models import AnonymousVoter


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_vote')
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='voters')
    anonymous_voter = models.ForeignKey(AnonymousVoter, on_delete=models.CASCADE, null=True, related_name='anonymous_votes')


    class Meta:
        unique_together = ("poll", "voted_by")


class VoteCount(models.Model):
    poll_vote = models.OneToOneField(Poll, on_delete=models.CASCADE, related_name='poll_vote_count')
    vote_count = models.PositiveIntegerField(default=0)