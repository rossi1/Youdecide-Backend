# Generated by Django 2.0.2 on 2019-07-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousvoter',
            name='username',
            field=models.CharField(max_length=60, null=True),
        ),
    ]