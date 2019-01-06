from django.shortcuts import render, redirect, reverse
from tickets.models import Bugs, Features, Comments


def view_cart(request): # Renders the cart page.

    cart = request.session.get('cart', {})
    
    return render(request, 'cart.html', {'cart': cart})
    
    
def add_to_cart(request, pk):
    """Add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if pk in cart:
        cart[pk] = int(cart[pk]) + quantity      
    else:
        cart[pk] = cart.get(pk, quantity) 
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
def adjust_cart(request, id):   # Adjust the quantitiy of whats in the cart. 
    quantity=int(request.POST.get('quantity'))
    cart=request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    