# Generated by Django 2.0.2 on 2019-10-14 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20190809_0248'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
