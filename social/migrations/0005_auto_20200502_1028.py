# Generated by Django 2.0.2 on 2020-05-02 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20200413_0335'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]