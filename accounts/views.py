from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')