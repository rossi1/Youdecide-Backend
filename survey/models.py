from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# # Create your models here.
# class Category(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     created_date = models.DateTimeField(auto_now_add=True)  # , default=timezone.now)
#     # updated = models.DateTimeField(auto_now=True)
#
#
# class SurveyQuestion(models.Model):
#     id = models.IntegerField(primary_key=True)
#     question = models.TextField()
#     opening_time = models.DateTimeField()
#     closing_time = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='survey_creator')
#     category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
#
#
# class SurveyCategories(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     survey_id = models.ForeignKey(SurveyQuestion, on_delete=models.SET_NULL, null=True, blank=True)
#     category_id = models.ManyToManyField(Category, related_name='survey_question_category', null=True, blank=True)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class SurveyQuestion(models.Model):
    survey_question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    created_by = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyCategories(models.Model):
    survey_categories_id = models.AutoField(primary_key=True)
    survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_categories'
        unique_together = (('survey', 'category'),)