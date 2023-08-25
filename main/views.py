from django.shortcuts import render
from products.models import Product
# Create your views here.


def home_page(request):
    trending_products = Product.objects.filter(trending=True)
    return render(request, 'main/home.html', {'trending_products': trending_products})

