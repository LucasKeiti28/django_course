from django.urls import paths
from django.urls.conf import path

from . import views

urlpatterns = [
    path('meetups/', views.index)
]