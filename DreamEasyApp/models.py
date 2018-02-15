# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime   

class Admin(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500, default='Add description of admin here')
    photo_url = models.CharField(max_length=200, default='http://www.stallerdental.com/wp-content/uploads/2016/12/user-icon.png')
    soundcloud_url = models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=280, default='Add description of artists here')
    photo_url = models.CharField(max_length=200, default='http://www.stallerdental.com/wp-content/uploads/2016/12/user-icon.png')
    soundcloud_url = models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.name

class SoundcloudPost(models.Model):
    name = models.CharField(max_length=200, default='Add the name of the release here')
    embed_link = models.CharField(max_length=2000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
