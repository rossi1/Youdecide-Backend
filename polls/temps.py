from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import random, base64


# class Options(models.Model):
#     option_text = models.CharField(max_length=100)

# set the width of the key
default_size = 2


def make_token(mysize=1):
    '''Computes an access token to an api randomly none deterministic.
    this test should always fail becuase is random value generation
    : param size: the width of the bytes
    : returns: a random token
    '''
    random_seed = random.SystemRandom()
    token_bytes = bytes(random_seed.randrange(0, 256) for index in range(18 * mysize))
    token_base64 = base64.urlsafe_b64encode(token_bytes)
    token_string = token_base64.decode('ascii')
    return token_string


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=250)
    CHOICES_TYPE = (
        ('TEXT', 'TEXT'),
        ('AUDIO', 'AUDIO'),
        ('VIDEO', 'VIDEO'),
    )
    choice_type = models.CharField(max_length=10, choices=CHOICES_TYPE, default='TEXT')
    # options = models.ForeignKey(Options, on_delete=models.CASCADE)

    def _get_unique_slug(self):
        url = self.question + "-" + make_token()
        slug = slugify(url)
        unique_slug = slug
        # num = 1
        # while Poll.objects.filter(slug=unique_slug).exists():
        #     unique_slug = '{}-{}'.format(slug, num)
        #     num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('-pub_date',)


class Choices(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # voter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='voters', blank=True, null=True)
    # vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("poll", "choice_text"),
            # no duplicated position per question
            # ("question", "position")
        ]   # order_with_respect_to = 'poll'


class Vote(models.Model):
    choice = models.ForeignKey(Choices, related_name='vote_choice', on_delete=models.CASCADE)
    # poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    # voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voters', blank=True, null=True,
    #  unique=True)
    voter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='voters', blank=True, null=True)
    # voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("voter",)

    def save(self, *args, **kwargs):
        self.vote_count += 1
        super().save(*args, **kwargs)


class PollDuration(models.Model):
    poll = models.OneToOneField(Poll, on_delete=models.CASCADE)
    duration = models.DateTimeField(default=None)     # '2006-10-25 14:30:59'


class ChoiceVotes(models.Model):
    choices = models.OneToOneField(Choices, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='choice_voters', blank=True, null=True)
    vote_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.vote_count += 1
        super().save(*args, **kwargs)


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
