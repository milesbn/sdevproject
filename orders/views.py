from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    cart = request.session.get('cart', {})
    cart_total = 0

    for id, item in cart.items():
        cart_total += float(item['price']) * item['quantity']

    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=int(cart_total*100),  
            currency="usd",
            source=request.POST['stripeToken']
        )
    return render(request, 'checkout.html', {'key': settings.STRIPE_PUBLIC_KEY, 'cart_total': cart_total})