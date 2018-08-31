# from django.db import models
# from django.contrib.auth.models import User
# from mambilla.abstract_models import StartEndDate, TimeStampModel
#
#
# # Create your models here.
# class Question(TimeStampModel):
#     question = models.CharField(max_length=140)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Answer(TimeStampModel):
#     answer = models.CharField(max_length=250)
#     by_user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Answers(models.Model):
#     answers = models.ForeignKey(Answer)
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Questions(models.Model):
    # In Question models we have created a slug field to make it more readable.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    group = models.ForeignKey('QuestionGroups', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

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
