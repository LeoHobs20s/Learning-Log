from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_view(request):
    """ view to render login authentication """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = LoginForm()
    else:
        # POST Data Submitted; process credentials
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}')
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
    context = {'form':form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')