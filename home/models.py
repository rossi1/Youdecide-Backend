# # Tracking# file by folder pattern:  migrations
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class ActionType(models.Model):
#     action_type_id = models.AutoField(primary_key=True)
#     actionname = models.CharField(max_length=20)
#     description = models.TextField(blank=True, null=True)
#     createddate = models.DateTimeField(blank=True, null=True)
#     changedate = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'action_type'
#
#
# class AnonymousVoter(models.Model):
#     anonymous_voter_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=60)
#     phone_number = models.CharField(max_length=16)
#     email_address = models.CharField(unique=True, max_length=255, blank=True, null=True)
#     survey_choice = models.ForeignKey('SurveyChoice', models.DO_NOTHING)
#     survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
#     useragent = models.TextField(db_column='userAgent', blank=True, null=True)  # Field name made lowercase.
#     devicename = models.CharField(db_column='deviceName', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     manufacturer = models.CharField(max_length=60, blank=True, null=True)
#     ip_address = models.CharField(max_length=40, blank=True, null=True)
#     browsername = models.CharField(db_column='browserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     browserversion = models.CharField(db_column='browserVersion', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     operatingsystem = models.CharField(db_column='operatingSystem', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     language = models.CharField(max_length=5, blank=True, null=True)
#     created_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'anonymous_voter'
#         unique_together = (('phone_number', 'survey'), ('email_address', 'survey'),)
#
#
# class Auditvault(models.Model):
#     auditvault_id = models.AutoField(primary_key=True)
#     userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
#     actiontypeid = models.ForeignKey(ActionType, models.DO_NOTHING, db_column='actiontypeid')
#     tablename = models.CharField(max_length=25, blank=True, null=True)
#     useragent = models.TextField(blank=True, null=True)
#     rowdataold = models.TextField(db_column='rowDataOld', blank=True, null=True)  # Field name made lowercase.
#     rowdatanew = models.TextField(db_column='rowDataNew', blank=True, null=True)  # Field name made lowercase.
#     logtime = models.DateTimeField(db_column='logTime', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'auditvault'
#
#
# class City(models.Model):
#     city_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='stateid')
#
#     class Meta:
#         managed = False
#         db_table = 'city'
#
#
# class Country(models.Model):
#     country_id = models.AutoField(primary_key=True)
#     shortcode_2 = models.CharField(max_length=6)
#     countryname = models.CharField(max_length=80)
#     nickname = models.CharField(max_length=80, blank=True, null=True)
#     shortcode_3 = models.CharField(max_length=6, blank=True, null=True)
#     numcode = models.SmallIntegerField(blank=True, null=True)
#     phone_code = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'country'
#
#
# class Currency(models.Model):
#     currency_id = models.AutoField(primary_key=True)
#     country = models.CharField(max_length=100)
#     currencyname = models.CharField(max_length=50)
#     currencycode = models.CharField(max_length=50, blank=True, null=True)
#     currencysymbol = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'currency'
#
#
# class SearchRegistry(models.Model):
#     search_registry_id = models.AutoField(primary_key=True)
#     keyword = models.CharField(max_length=255)
#     tags = models.CharField(max_length=255, blank=True, null=True)
#     tablename = models.CharField(max_length=255, blank=True, null=True)
#     rowid = models.IntegerField(blank=True, null=True)
#     logtime = models.DateTimeField(db_column='logTime', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'search_registry'
#
#
# class State(models.Model):
#     state_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryid')
#
#     class Meta:
#         managed = False
#         db_table = 'state'
#
#
# class SurveyCategories(models.Model):
#     survey_categories_id = models.AutoField(primary_key=True)
#     survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
#     category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'survey_categories'
#         unique_together = (('survey', 'category'),)
#
#
# class SurveyChoice(models.Model):
#     survey_choice_id = models.AutoField(primary_key=True)
#     survey = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
#     option = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'survey_choice'
#
#
# class SurveyChoiceImage(models.Model):
#     survey_choice_image_id = models.AutoField(primary_key=True)
#     survey_choice = models.ForeignKey(SurveyChoice, models.DO_NOTHING)
#     mediafilename = models.CharField(max_length=50)
#     mediasource = models.CharField(max_length=80, blank=True, null=True)
#     media = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'survey_choice_image'
#
#
# class SurveyQuestion(models.Model):
#     survey_question_id = models.AutoField(primary_key=True)
#     question = models.TextField()
#     opening_time = models.DateTimeField()
#     closing_time = models.DateTimeField()
#     created_by = models.IntegerField()
#     created_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'survey_question'
#
#
# class SurveyVote(models.Model):
#     survey_vote_id = models.AutoField(primary_key=True)
#     voter_type = models.ForeignKey('VoterType', models.DO_NOTHING)
#     voter_user_id = models.IntegerField()
#     survey_choice = models.ForeignKey(SurveyChoice, models.DO_NOTHING)
#     survey = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
#     created_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'survey_vote'
#         unique_together = (('voter_type', 'voter_user_id', 'survey'),)
#
#
# class Timezone(models.Model):
#     timezone_id = models.IntegerField(primary_key=True)
#     countrycode = models.CharField(db_column='CountryCode', max_length=6)  # Field name made lowercase.
#     coordinates = models.CharField(db_column='Coordinates', max_length=15)  # Field name made lowercase.
#     timezone = models.CharField(max_length=32)
#     comments = models.CharField(max_length=85)
#     utcoffset = models.CharField(db_column='UTCoffset', max_length=8)  # Field name made lowercase.
#     utcdstoffset = models.CharField(db_column='UTCDSToffset', max_length=8)  # Field name made lowercase.
#     notes = models.CharField(max_length=79, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'timezone'
#
#
# class UserAccountRecovery(models.Model):
#     user_account_recovery_id = models.AutoField(primary_key=True)
#     userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
#     question = models.CharField(max_length=100)
#     answer = models.CharField(max_length=100)
#     createddate = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user_account_recovery'
#
#
# class UserType(models.Model):
#     user_type_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     createddate = models.DateTimeField(blank=True, null=True)
#     lastupdated = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user_type'
#
#
# class Users(models.Model):
#     users_id = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=225)
#     password = models.CharField(max_length=255)
#     usertypeid = models.ForeignKey(UserType, models.DO_NOTHING, db_column='usertypeid')
#     userstatus = models.IntegerField(blank=True, null=True)
#     createddate = models.DateTimeField(blank=True, null=True)
#     lastupdated = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#
#
# class VoterType(models.Model):
#     voter_type_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=9)
#     created_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'voter_type'
