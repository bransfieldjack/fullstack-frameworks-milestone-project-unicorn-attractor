from django.shortcuts import render, redirect, reverse, get_object_or_404
from tickets.models import Bugs, Features, Comments
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
import stripe


stripe.api_key = settings.STRIPE_SECRET # For use with the stripe API. Stored in an environmen variable. env.py


def view_cart(request): # Renders the cart page.
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})
    
    
@login_required()
def checkout(request):
    
    """
    Handles checkout, retrieves cart contents from contexts file. Calculates price based on quantity and cost. Handles stripe payment and returns messages via django messages. 
    """
    
    if request.method=='POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                feature = get_object_or_404(Features, pk=id)
                total += quantity * 0.50
                order_line_item = OrderLineItem(order=order, feature=feature, quantity=quantity)
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(amount = int(total * 100), currency = "EUR", description = request.user.email, card = payment_form.cleaned_data['stripe_id'],)
            except stripe.error.CardError:
                    messages.error(request, "Your card has been declined. ")
                
            if customer.paid:
                messages.success(request, "You have successfully paid. ")
                request.session['cart'] = {}
                return redirect(reverse('checkout'))
            else:
                messages.error(request, "Unable to take payment. ")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card. ")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    
    
def add_to_cart(request, pk):
    
    """
    Add item to the cart. 
    """
    
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if pk in cart:
        cart[pk] = int(cart[pk]) + quantity      
    else:
        cart[pk] = cart.get(pk, quantity) 
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
def adjust_cart(request, id): 
    
    """
    Adjust the quantitiy of whats in the cart.
    """
    
    quantity=int(request.POST.get('quantity'))
    cart=request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    