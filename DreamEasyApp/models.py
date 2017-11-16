# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    soundcloud_url = models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.name
