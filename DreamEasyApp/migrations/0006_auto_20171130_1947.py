# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-30 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamEasyApp', '0005_auto_20171126_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='soundcloud_url',
            field=models.CharField(default='', max_length=100),
        ),
    ]