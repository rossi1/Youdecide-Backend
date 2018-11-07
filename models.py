Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountProfile(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=100)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'account_profile'


class ActionType(models.Model):
    actionname = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    changedate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_type'


class AnonymousVoter(models.Model):
    username = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=16)
    email_address = models.CharField(unique=True, max_length=255, blank=True, null=True)
    survey_choice = models.ForeignKey('SurveyChoice', models.DO_NOTHING)
    survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    useragent = models.TextField(db_column='userAgent', blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='deviceName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(max_length=60, blank=True, null=True)
    ip_address = models.CharField(max_length=40, blank=True, null=True)
    browsername = models.CharField(db_column='browserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    browserversion = models.CharField(db_column='browserVersion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(db_column='operatingSystem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(max_length=5, blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anonymous_voter'
        unique_together = (('phone_number', 'survey'), ('email_address', 'survey'),)


class ApiAdminuser(models.Model):
    admin_user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_adminuser'


class ApiAuditvault(models.Model):
    row_id = models.BigIntegerField()
    row_data_old = models.TextField()
    row_data_new = models.TextField()
    system_info = models.TextField()
    log_time = models.DateField()
    action_type_id = models.ForeignKey('ApiUseractiontype', models.DO_NOTHING)
    user_id = models.ForeignKey(ApiAdminuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_auditvault'


class ApiSurvey(models.Model):
    survey_name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    survey_category_id = models.ForeignKey('ApiSurveycategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_survey'


class ApiSurveycategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_surveycategory'


class ApiSurveyquestion(models.Model):
    question = models.TextField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    description = models.TextField()
    created_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    survey_id = models.ForeignKey(ApiSurvey, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_surveyquestion'


class ApiSurveyquestionorder(models.Model):
    question_order = models.IntegerField()
    question_id = models.ForeignKey(ApiSurveyquestion, models.DO_NOTHING)
    survey_id = models.ForeignKey(ApiSurvey, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_surveyquestionorder'


class ApiSurveyrespondent(models.Model):
    ip_address = models.CharField(max_length=39)
    created_date = models.DateTimeField()
    surveyor = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_surveyrespondent'


class ApiSurveyresponse(models.Model):
    start_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    respondent_id = models.ForeignKey(ApiSurveyrespondent, models.DO_NOTHING)
    survey_id = models.ForeignKey(ApiSurvey, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_surveyresponse'


class ApiSurveyresponsechoice(models.Model):
    response_choice = models.TextField()
    question_id = models.ForeignKey(ApiSurveyquestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_surveyresponsechoice'


class ApiUseractiontype(models.Model):
    action_name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(ApiAdminuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_useractiontype'


class ApiUsertype(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'api_usertype'


class Auditvault(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    actiontypeid = models.ForeignKey(ActionType, models.DO_NOTHING, db_column='actiontypeid')
    tablename = models.CharField(max_length=25, blank=True, null=True)
    useragent = models.TextField(blank=True, null=True)
    rowdataold = models.TextField(db_column='rowDataOld', blank=True, null=True)  # Field name made lowercase.
    rowdatanew = models.TextField(db_column='rowDataNew', blank=True, null=True)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='logTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditvault'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    poll = models.ForeignKey('PollsPoll', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsPoll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_poll'


class PollsPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_post'


class PollsVote(models.Model):
    choice = models.ForeignKey(PollsChoice, models.DO_NOTHING)
    poll = models.ForeignKey(PollsPoll, models.DO_NOTHING)
    voted_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_vote'
        unique_together = (('poll', 'voted_by'),)


class SearchRegistry(models.Model):
    keyword = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(max_length=255, blank=True, null=True)
    rowid = models.IntegerField(blank=True, null=True)
    logtime = models.DateTimeField(db_column='logTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_registry'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SurveyCategories(models.Model):
    survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_categories'
        unique_together = (('survey', 'category'),)


class SurveyCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_category'


class SurveyChoice(models.Model):
    survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    option = models.TextField()

    class Meta:
        managed = False
        db_table = 'survey_choice'


class SurveyChoiceImage(models.Model):
    survey_choice = models.ForeignKey(SurveyChoice, models.DO_NOTHING)
    mediafilename = models.CharField(max_length=50)
    mediasource = models.CharField(max_length=80, blank=True, null=True)
    media = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_choice_image'


class SurveyQuestion(models.Model):
    question = models.TextField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    created_by = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveySurveycategories(models.Model):
    survey_id = models.ForeignKey('SurveySurveyquestion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_surveycategories'


class SurveySurveycategoriesCategoryId(models.Model):
    surveycategories = models.ForeignKey(SurveySurveycategories, models.DO_NOTHING)
    category = models.ForeignKey(SurveyCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_surveycategories_category_id'
        unique_together = (('surveycategories', 'category'),)


class SurveySurveyquestion(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    category_id = models.ForeignKey(SurveyCategory, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_surveyquestion'


class SurveyVote(models.Model):
    voter_type = models.ForeignKey('VoterType', models.DO_NOTHING)
    voter_user_id = models.IntegerField()
    survey_choice = models.ForeignKey(SurveyChoice, models.DO_NOTHING)
    survey = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_vote'
        unique_together = (('voter_type', 'voter_user_id', 'survey'),)


class UserAccountRecovery(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    createddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account_recovery'


class UserType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type'


class UserprofileUserprofile(models.Model):
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    user_from = models.ForeignKey(AuthUser, models.DO_NOTHING)
    user_to = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userprofile_userprofile'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=225)
    password = models.CharField(max_length=255)
    usertypeid = models.ForeignKey(UserType, models.DO_NOTHING, db_column='usertypeid')
    userstatus = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VoterType(models.Model):
    survey_id = models.IntegerField()
    title = models.CharField(max_length=9)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voter_type'


class VotingAnswers(models.Model):
    answer_text = models.TextField()
    is_anonymous = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    question = models.ForeignKey('VotingQuestions', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voting_answers'


class VotingPostpoll(models.Model):
    title = models.CharField(max_length=140)
    votes = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voting_postpoll'


class VotingQuestiongroups(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'voting_questiongroups'


class VotingQuestions(models.Model):
    title = models.TextField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    slug = models.CharField(max_length=50)
    group = models.ForeignKey(VotingQuestiongroups, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voting_questions'


class VotingUservotes(models.Model):
    vote_type = models.CharField(max_length=140)
    post = models.ForeignKey(VotingPostpoll, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voting_uservotes'
        unique_together = (('vote_type', 'post', 'user'),)
