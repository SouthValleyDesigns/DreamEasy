<<<<<<< HEAD
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
=======
from django.conf.urls import url, include
from DreamEasyApp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^art/', views.art),
    url(r'^members/', views.members),
>>>>>>> d54b61c1e378d59f102731a75507dc20f1c551b4
]
