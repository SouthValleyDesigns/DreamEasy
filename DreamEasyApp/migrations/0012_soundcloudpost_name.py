# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-15 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamEasyApp', '0011_soundcloudpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundcloudpost',
            name='name',
            field=models.CharField(default='Add the name of the release here', max_length=200),
        ),
    ]
