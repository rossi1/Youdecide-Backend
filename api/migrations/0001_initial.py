# Generated by Django 2.0.5 on 2018-11-04 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_admin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AuditVault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.BigIntegerField()),
                ('row_data_old', models.BinaryField()),
                ('row_data_new', models.BinaryField()),
                ('system_info', models.BinaryField()),
                ('log_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='')),
                ('opening_time', models.DateTimeField(auto_now=True)),
                ('closing_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_user_question', to='api.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_order', models.IntegerField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_question_key', to='api.SurveyQuestion')),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_question_order', to='api.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyRespondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='user_ip_address')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('surveyor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('respondent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveyResponse_respondent', to='api.SurveyRespondent')),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveyResponse_survey', to='api.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResponseChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_choice', models.TextField(default='')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_question_choice', to='api.SurveyQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='UserActionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionType_adminuser', to='api.AdminUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_category', to='api.SurveyCategory'),
        ),
        migrations.AddField(
            model_name='auditvault',
            name='action_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditvault_actiontype', to='api.UserActionType'),
        ),
        migrations.AddField(
            model_name='auditvault',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audtivault_adminuser', to='api.AdminUser'),
        ),
    ]
