from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # The user wants to signup
        if request.POST['password'] == request.POST['password1']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'User name has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # user has entered data
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})
    else:
        # the user is requesting for the login page
        return render(request, 'accounts/login.html')

def logout(request):
    # TODO Need to route to homepage after logging out
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')