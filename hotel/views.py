from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import *


room_numbers = [
    ('101', '101'),
    ('102', '102'),
    ('103', '103'),
    ('104', '104'),
    ('201', '201'),
    ('202', '202'),
    ('203', '203'),
    ('204', '204'),
]


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/guest/")
        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')


def add_guest(request):

    if request.method == "POST":

        Guests.objects.create(
            name=request.POST['name'],
            mobile_number=request.POST['mobile_number'],
            p_address=request.POST['p_address'],
            aadhar_ID=request.POST['aadhar_ID']
        )

        return redirect('/room/')

    return render(request, 'add_guests.html')


def add_room(request):

    if request.method == "POST":

        is_available = 'is_available' in request.POST

        Room.objects.create(
            room_number=request.POST['room_number'],
            is_available=is_available
        )

        return redirect('/booking/')

    return render(request, 'add_room.html', {
        'room_numbers': room_numbers
    })


def add_booking(request):

    if request.method == "POST":

        check_in = request.POST['check_in']
        check_out = request.POST['check_out']

        # Get today's date
        today = timezone.localdate()

        # Convert strings from HTML into actual dates
        from datetime import datetime

        check_in_date = datetime.strptime(
            check_in, '%Y-%m-%d'
        ).date()

        check_out_date = datetime.strptime(
            check_out, '%Y-%m-%d'
        ).date()

        # Don't allow check-in in the past
        if check_in_date < today:
            return render(request, 'add_booking.html', {
                'error': 'Check-in date cannot be in the past.',
                'guests': Guests.objects.all(),
                'rooms': Room.objects.filter(is_available=True)
            })

        # Don't allow check-out in the past
        if check_out_date < today:
            return render(request, 'add_booking.html', {
                'error': 'Check-out date cannot be in the past.',
                'guests': Guests.objects.all(),
                'rooms': Room.objects.filter(is_available=True)
            })

        # Check-out should not be before check-in
        if check_out_date < check_in_date:
            return render(request, 'add_booking.html', {
                'error': 'Check-out date cannot be before check-in date.',
                'guests': Guests.objects.all(),
                'rooms': Room.objects.filter(is_available=True)
            })

        guest = Guests.objects.get(
            id=request.POST['guest']
        )

        room = Room.objects.get(
            id=request.POST['room']
        )

        Booking.objects.create(
            guest=guest,
            room_number=room,
            check_in=check_in_date,
            check_out=check_out_date
        )

        return redirect('/bookings/')

    guests = Guests.objects.all()
    rooms = Room.objects.filter(is_available=True)

    return render(request, 'add_booking.html', {
        'guests': guests,
        'rooms': rooms
    })

def booking(request):

    all_bookings = Booking.objects.all()

    return render(request, 'bookings.html', {
        'bookings': all_bookings
    })