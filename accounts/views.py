from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def login(request):
    
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out. ')
    return redirect(reverse('index'))
    
    
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)  # Instantiate the user registration form and pass the post request value. 
        
        if registration_form.is_valid():
            user = registration_form.save()
            
            user = auth.authenticate(username=request.POST["username"], password = request.POST["password1"]) # Passes the reg form with the username/password. 
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered. ") # If registration is successful.
                return redirect(reverse('tickets'))
            else:
                messages.error(request, "Unable to register your account.")
        
    registration_form = UserRegistrationForm()
    return render(request, 'register.html', {'registration_form': registration_form})
    
    
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})
    
    