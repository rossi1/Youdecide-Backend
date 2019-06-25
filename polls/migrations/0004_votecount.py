# Generated by Django 2.0.2 on 2019-06-25 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190624_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('poll_vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Vote')),
            ],
        ),
    ]