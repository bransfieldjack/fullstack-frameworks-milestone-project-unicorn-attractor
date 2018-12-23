from django.shortcuts import render, HttpResponse, redirect


def tickets(request):
    return render(request, 'tickets.html')
    
    
def bugs(request):
    return render(request, 'bugs.html')
    
    
def features(request):
    return render(request, 'features.html')
    
    
def add_bug(request):
    return render(request, 'add_bug.html')
    
    
def add_feature(request):
    return render(request, 'add_feature.html')