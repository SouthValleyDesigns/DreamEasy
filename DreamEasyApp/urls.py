from django.conf.urls import url, include
from DreamEasyApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^art/', views.art, name='art'),
    url(r'^members/', views.members, name='members'),
    url(r'^contact/', views.contact, name='contact'),
]
