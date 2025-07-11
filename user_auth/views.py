from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from user_auth.models import User
from .forms import LoginForm, SigupForm

def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            print("User authenticated successfully")
            print(f"User email: {user.email}")
            # Redirect to a success page.
            return redirect('/') 
        else:
            form.add_error(None, "Invalid credentials")

    return render(request, 'login.html', {'form': form})

def create_user_view(request):
    form  = SigupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match")
        else:
            User.objects.create_user(email=email, password=password)
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def home_view(request): 
    if request.user.is_authenticated:
        print("User is authenticated")
        print(f"User email: {request.user.email}")
        return render(request, 'home.html', {'user': request.user})
    else:
        print("User is not authenticated")
        print("Redirecting to login")
        return redirect('login')
    
def logout_view(request):
    if request.user.is_authenticated:
        print("User is authenticated, logging out")
        logout(request)
    else:
        print("User is not authenticated, no action taken")
    return redirect('login')
