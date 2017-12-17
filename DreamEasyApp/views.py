# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member, Admin
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def members(request):
    member_list = Member.objects.order_by('name')
    admin_list = Admin.objects.order_by('name')

    return render(request, 'members.html', {
        'member_list':member_list,
        'admin_list':admin_list,
        })


def store(request):
    return render(request, 'store.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return render(request, "index.html")

    return render(request, "contact.html", {'form': form})
