from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from account.models import CustomUser

# from django_mysql.models import ListCharField

# Create your models here.
'''
///
the user model will have the following objects:
USER:- EMAIL, PASSWORD, USERNAME
VOTER- VOTER-ID, VOTER IP-ADDRESS
POLL:-  CREATOR(USER), QUESTION, LOCATION, WHEN_CREATED, APPROVAL-BOOLEAN
QUESTION:- QUESTION, OPTIONS, QUESTION_ID(OR SLUG for URL for sharing)
CHOICES:- {OPTION_A: [A_COUNTS, A_PERCENT], OPTION_B: [B_COUNTS, B_PERCENT], ..., OPTION_N:
            [N_COUNTS, N_PERCENT]}
RULES:-APPROVAL, FILTER- SIMILAR POLLS!!!
RESULT or SUMMARY:- CHOICES,  WHEN_CREATED, START_DATE, END_DATE, TOTAL_VOTES,
POLLS: LIST OF POLL -


/// stackover flow answer on preventing duplicate voting


Depends on how far you want to take it:

    Submit the votes through ajax using POST method so there is no url to access directly from a browser
    Add cookies for those who voted
    Add captcha
    Store IPs (here are some suggestions on how to store them efficiently, can also utilize something
    like Redis if performance is critical, but unless you are building a national voting system you probably would be
    just fine with a regular table)
    Require registration to vote (registration with email confirmation, registration with facebook account,
    registration with sms confirmation, and so on)


    "save the vote and thank the voter"

Also whenever you detected a user has already voted, it could be a smart move to just silently ignore their further
votes and pretend that they were accepted, this way they won't try nearly as hard to cheat.

///

polls
'''


class UserType(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField(default="")


class AdminUser(models.Model):
    '''
    # the following info has been provided by the default django.contrib.models.auth.User
    user_type_id = models.ForeignKey(UserType, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    '''
    admin_user = models.ForeignKey(CustomUser, related_name='custom_admin_user', on_delete=models.CASCADE)


class SurveyCategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(default="")
    created_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)


class Survey(models.Model):
    survey_category_id = models.ForeignKey(SurveyCategory, related_name='survey_category', on_delete=models.CASCADE)
    survey_name = models.CharField(max_length=50)
    description = models.TextField(default="")
    created_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)


class SurveyQuestion(models.Model):
    survey_id = models.ForeignKey(Survey, related_name='survey_user_question', on_delete=models.CASCADE)
    question = models.TextField(default="")
    opening_time = models.DateTimeField(auto_now=True)
    closing_time = models.DateTimeField(auto_now=True)
    description = models.TextField(default="")
    created_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)


class SurveyResponseChoice(models.Model):
    question_id = models.ForeignKey(SurveyQuestion, related_name='survey_question_choice', on_delete=models.CASCADE)
    response_choice = models.TextField(default="")


class SurveyQuestionOrder(models.Model):
    survey_id = models.ForeignKey(Survey, related_name='survey_question_order', on_delete=models.CASCADE)
    question_id = models.ForeignKey(SurveyQuestion, related_name='survey_question_key', on_delete=models.CASCADE)
    question_order = models.IntegerField()


class SurveyRespondent(models.Model):
    '''
    ### this info is provided by creating a subclass of django auth.User object
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.TextField(default="")
    '''
    surveyor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # ip_address = models.TextField(default="")
    # django has inbuilt GenericIPAddressField with support for validation
    ip_address = models.GenericIPAddressField(verbose_name='user_ip_address')
    created_date = models.DateTimeField(auto_now=True)


class SurveyResponse(models.Model):
    survey_id = models.ForeignKey(Survey, related_name='surveyResponse_survey', on_delete=models.CASCADE)
    respondent_id = models.ForeignKey(SurveyRespondent, related_name='surveyResponse_respondent', on_delete=models.CASCADE)
    start_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)


class UserActionType(models.Model):
    created_by = models.ForeignKey(AdminUser, related_name='actionType_adminuser', on_delete=models.CASCADE)
    action_name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)


class AuditVault(models.Model):
    user_id = models.ForeignKey(AdminUser, related_name='audtivault_adminuser', on_delete=models.CASCADE)
    action_type_id = models.ForeignKey(UserActionType, related_name='auditvault_actiontype', on_delete=models.CASCADE)
    row_id = models.BigIntegerField(null=False)
    row_data_old = models.BinaryField()
    row_data_new = models.BinaryField()
    system_info = models.BinaryField()
    log_time = models.DateField(auto_now=True)


'''
polls

# class User(AbstractUser):
#     full_name = models.TextField(max_length=500, blank=True)
#     email = models.EmailField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)


class VoterId(models.Model):
    voterID = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(max_length=100)


class Question(models.Model):
    # creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    # options = models.ForeignKey(Choice)
    # created_on = models.DateTimeField(auto_now_add=True)


class Poll(models.Model):
    #  question = models.ForeignKey(Question)             # models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255)
    approved = models.BooleanField(True)


class Choice(models.Model):
    #  poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    '''
