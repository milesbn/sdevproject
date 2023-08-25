from django.urls import path
from . import views
from .views import cart_view, update_cart

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('update-cart/<int:id>/', views.update_cart, name='update_cart'),
]