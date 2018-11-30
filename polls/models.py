from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('-pub_date',)


class Choices(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class PollDuration(models.Model):
    poll = models.OneToOneField(Poll, on_delete=models.CASCADE)
    duration = models.DateTimeField(default=None)


# class Vote(models.Model):
#     choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
#     voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ("poll", "voted_by")


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
