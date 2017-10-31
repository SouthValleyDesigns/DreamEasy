# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def members(request):
    return render(request, 'members.html')

def art(request):
    return render(request, 'art.html')

def contact(request):
    return render(request, 'contact.html')
