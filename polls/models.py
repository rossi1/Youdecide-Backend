from django.db import models
from django.contrib.auth.models import User

from anonymous_user.models import AnonymousVoter

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
    expire_date = models.DateTimeField(blank=True, null=True) #creata a function to return duration of a poll
    has_expired  = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250)
    #CHOICES_TYPE = (
        #('TEXT', 'TEXT'),
        #('AUDIO', 'AUDIO'),
        #('VIDEO', 'VIDEO'),
    #)
    #choice_type = models.CharField(max_length=10, choices=CHOICES_TYPE, default='TEXT')
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

    def __str__(self):
        return str(self.choice) 