# Generated by Django 2.0.4 on 2018-11-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyCategories',
            fields=[
                ('survey_categories_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'survey_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('survey_question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('opening_time', models.DateTimeField()),
                ('closing_time', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'survey_question',
                'managed': False,
            },
        ),
    ]
