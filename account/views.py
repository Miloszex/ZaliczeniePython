from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'account/register_completed.html',{'user':user})
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html',{'form':form})


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'account/login_success.html', {'user':user})
        else:
            return render(request, 'account/login_error.html',{'message':'Login Error! , Invalid Data'})
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html',{'form':form})


def logout_user(request):
    logout(request)
    return render(request, 'account/logout.html', {'message':'You have been logged out successfully'})