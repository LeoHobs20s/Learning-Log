from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .forms import LoginForm, RegistrationForm


def login_view(request):
    """ view to render login authentication """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = LoginForm()
    else:
        # POST Data Submitted; process credentials
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # validate user credentials
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # create a session for the current user
                login(request, user)
                messages.success(request, f'Welcome, {user.username}')
                return redirect('index') # sending user to home page
            else:
                messages.error(request, 'Invalid credentials')
    context = {'form':form}
    return render(request, 'users/login.html', context)


def logout_view(request):
    """ Logout the current user in session """

    # remove information of the current user from the session
    logout(request)
    return redirect('login_view')


def register(request):
    """ Registering new user in the site """

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = RegistrationForm()
    
    else:
        # POST Data Submitted; process the user's information
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # authenticate and login user
            user = authenticate(username=new_user.username, password=request.POST['password1'])
            # login(request, user)
            return redirect('login_view') # sending user to login page
    
    context = {'form':form}
    return render(request, 'users/register.html', context)