from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile


def index(request):
    
    """
    User index function, returning the index page. 
    """
    return render(request, 'index.html')


def login(request): 
    
    """
    This function handles user login, returning the login page and form. 
    If the users login is successful they are redirected to the above index function, if not they are presented with an error message.
    """
    
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
    
    """
    Handles the request for a user to login. Only accessible if the user has logged in to begin with.
    Uses the built in django auth functionality and django messages. 
    """
    
    auth.logout(request)
    messages.success(request, 'You have been logged out. ')
    return render(request, 'logout.html')
    
    
def register(request):
    
    """
    Handles user registration. Checks if a user is authenticated, then redirects. If not, displayed django messages error. 
    """
    
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
    
    """
    Handles creation of user profile page/form. The model for this function will extend django auth. 
    """

    if request.method=="POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect(user_profile)
    else:
        form = UserProfileForm
        
        profile = Profile.objects.get()
        
    return render(request, 'user_profile.html', {'form': form, 'profile': profile})