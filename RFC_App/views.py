from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request,"landingPage.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            #customer_group = Group.objects.get(name='Customer')
            #customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #yikes, on that data per parameter for authform
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landingPage')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

def forum(request):
    return render(request,"forum.html")
