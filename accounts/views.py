from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out. ')
    return redirect(reverse('index'))
    
    
def register(request):
    return render(request, 'register.html')
    
    
