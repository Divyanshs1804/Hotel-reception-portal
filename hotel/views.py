from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("booking/")  # wherever a logged-in user should land
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def booking(request):
    return render(request, 'booking.html')