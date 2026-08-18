from django.contrib import admin
from django.urls import path, include
from hotel.views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('login/', user_login, name='login'),
    path('', index, name='index'),
    path('booking/', booking, name='booking'),
    path('guest/', add_guest, name='add_guest'),
    path('room/', add_room, name='add_room'),
    path('new-booking/', add_booking, name='add_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'
),
]