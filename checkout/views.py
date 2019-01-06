from django.shortcuts import render
from tickets.models import Bugs, Features, Comments


def cart(request):
    
    return render(request, 'cart.html')