from django.shortcuts import render, HttpResponse, redirect
from .models import Bugs, Features


def tickets(request):
    return render(request, 'tickets.html')
    
    
def bugs(request):
    bugs = Bugs.objects.all()
    
    return render(request, 'bugs.html', {'bugs': bugs})
    
    
def features(request):
    features = Features.objects.all()
    
    return render(request, 'features.html', {'features': features})
    
    
def add_bug(request):
    return render(request, 'add_bug.html')
    
    
def add_feature(request):
    return render(request, 'add_feature.html')