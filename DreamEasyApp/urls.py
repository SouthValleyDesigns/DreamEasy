from django.conf.urls import url, include
from DreamEasyApp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^art/', views.art),
    url(r'^members/', views.members),
]
