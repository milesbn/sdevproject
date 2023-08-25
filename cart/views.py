from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']
    product_id = str(product_id)  

    if product_id not in cart:
        cart[product_id] = {'quantity': int(request.POST['quantity']), 'title': product.title, 'price': float(product.price)}
    else:
        cart[product_id]['quantity'] += int(request.POST['quantity'])

    request.session['cart'] = cart
    request.session.modified = True 

    return redirect('cart:cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = {id: get_object_or_404(Product, pk=id) for id in cart.keys()}
    return render(request, 'cart/cart.html', {'cart': cart, 'products': products})

def update_cart(request, id):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    if request.method == "POST":
        if request.POST['action'] == 'increase':
            request.session['cart'][str(id)]['quantity'] += 1
        elif request.POST['action'] == 'decrease':

            if request.session['cart'][str(id)]['quantity'] == 1:

                del request.session['cart'][str(id)]
                if len(request.session['cart'])==0:
                    del request.session['cart']
            else:
                request.session['cart'][str(id)]['quantity'] -= 1

        request.session.modified = True

    return redirect('cart:cart')