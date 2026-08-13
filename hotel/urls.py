from django.contrib import admin
from django.urls import path, include 
from hotel.views import *

urlpatterns = [
    path('about/', about , name = 'about'),
    path('login/', user_login, name='login'),
    path('', index, name = 'index'),
    path('booking/', booking, name = 'booking')
]