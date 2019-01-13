from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import Profile


class UserLoginForm(forms.Form):    # User login form, taking tw fields - username, password. 
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class UserRegistrationForm(UserCreationForm):   # User registration form, allowing for users to register.
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):  # Clean prevents dirty/used data in the DB. 
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(email=email).exclude(username=username): # Filter through the DB looking for a user with the same username. 
            raise forms.ValidationError('Email address already exists. ')
        return email
        
    def clean_password2(self):  # Clean prevents dirty/used data in the DB. 
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if not password1 or not password2:
            raise ValidationError("Confirm Password.")
            
        if password1 != password2:
            raise ValidationError("Passwords must match!")
            
        return password2
        
        
class UserProfileForm(forms.ModelForm): # User profile input form, to be implemented in a future iteration. 
    
    class Meta:
        model = Profile
        fields = ('email', 'bio', 'location', 'birth_date', 'website', 'publicinfo')