# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-14 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamEasyApp', '0008_member_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default='Add description of admin here', max_length=2500)),
                ('photo_url', models.CharField(default='http://www.stallerdental.com/wp-content/uploads/2016/12/user-icon.png', max_length=200)),
                ('soundcloud_url', models.CharField(default='#', max_length=100)),
            ],
        ),
    ]