from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import IntegrityError


class Questions(models.Model):
    # In Question models we have created a slug field to make it more readable.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    group = models.ForeignKey('QuestionGroups', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    # We have also given flexibility for the user to save its answer anonymously.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Answers'


class QuestionGroups(models.Model):
    # QuestionGroup is kept to differentiate question of different topics.
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'QuestionGroups'


class PostPoll(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    votes = models.IntegerField(default=0)

    def upvote(self, user):
        try:
            self.post_votes.create(user=user, post=self, vote_type="up")
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'
        return 'ok'

    def downvote(self, user):
        try:
            self.post_votes.create(user=user, post=self, vote_type="down")
            self.votes -= 1
            self.save()
        except IntegrityError:
            return 'already_downvoted'
        return 'ok'


class UserVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_votes")
    post = models.ForeignKey(PostPoll, on_delete=models.CASCADE, related_name="post_votes")
    vote_type = models.CharField(max_length=140)

    class Meta:
        unique_together = ('user', 'post', 'vote_type')
