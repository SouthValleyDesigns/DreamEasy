# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Member, Admin


def index(request):
    return render(request, 'index.html')


def members(request):
    member_list = Member.objects.order_by('name')
    admin_list = Admin.objects.order_by('name')

    return render(request, 'members.html', {
        'member_list':member_list,
        'admin_list':admin_list,
        })


def art(request):
    return render(request, 'art.html')


def contact(request):
    return render(request, 'contact.html')
