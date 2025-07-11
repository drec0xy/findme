from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from user_auth.models import User
from .forms import LoginForm, SigupForm

def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            form.add_error(None, "Invalid credentials")

    return render(request, 'login.html', {'form': form})

def create_user_view(request):
    form  = SigupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match")
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'signup.html', {'form': form})
