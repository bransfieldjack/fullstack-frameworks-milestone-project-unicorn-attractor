from django.shortcuts import get_object_or_404
from tickets.models import Features


def cart_contents(request): #  Allows the contents of the cart to be displayed on all pages of the app. Creating a context that is available to all pages. 
    
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    feature_count = 0
    
    for id, quantity in cart.items():    # ID of the feature and quantity of the feature. (Should usually only be a quantity of 1)
        feature = get_object_or_404(Features, pk=id)
        total += quantity * 5.00
        feature_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'feature': feature})
  
    return { 'cart_items': cart_items, 'total': total, 'feature_count': feature_count}