from django.contrib import admin
from django.urls import path, include 
from hotel.views import *
urlpatterns = [
    path('about/', about , name = 'about')
]