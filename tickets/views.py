from django.shortcuts import render, HttpResponse, redirect


def tickets(request):
    return render(request, 'tickets.html')