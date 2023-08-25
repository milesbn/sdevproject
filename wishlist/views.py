from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.http import JsonResponse

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if 'wishlist' not in request.session:
        request.session['wishlist'] = {}

    wishlist = request.session['wishlist']
    product_id = str(product_id)  

    if product_id not in wishlist:
        wishlist[product_id] = {'title': product.title, 'price': float(product.price)}
 
    request.session['wishlist'] = wishlist
    request.session.modified = True 

    return redirect('wishlist:wishlist_view')

def wishlist_view(request):
    wishlist = request.session.get('wishlist', {})
    products = {id: get_object_or_404(Product, pk=id) for id in wishlist.keys()}
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist, 'products': products})

def delete_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = request.session.get('wishlist', {})

    product_id = str(product_id)
    if product_id in wishlist:
        del wishlist[product_id]
        request.session['wishlist'] = wishlist
        request.session.modified = True
       
    return JsonResponse({'success': True})