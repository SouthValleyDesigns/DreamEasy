# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-26 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamEasyApp', '0003_remove_member_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(default='google.com', upload_to=b''),
        ),
    ]
