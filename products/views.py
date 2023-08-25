from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def browse(request):
    products_list = Product.objects.all() 

    paginator = Paginator(products_list, 18)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'browse.html', {'page_obj': page_obj}) 


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def home(request):
    trending_products = Product.objects.filter(trending=True)
    new_products = Product.objects.filter(is_new=True)
    return render(request, "home.html", {"new_products": new_products})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        rating = float(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
    return redirect('products:product_detail', id=product.id)

