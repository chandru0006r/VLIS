from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'authenticate/home.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('adminlogin')
    else:
        return render(request, 'authenticate/adminlogin.html')
    
def login_user(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(otp)
        user = authenticate(request, username="user", password="pass")
        
        if otp=="1234":
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, "OTP is incorrect !!")
            return redirect('userlogin')
    else:
        return render(request, 'authenticate/userlogin.html')



def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


