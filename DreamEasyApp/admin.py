# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Member, Admin, SoundcloudPost

admin.site.register(Member)
admin.site.register(Admin)
admin.site.register(SoundcloudPost)
