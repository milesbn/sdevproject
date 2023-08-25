from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('browse/', views.browse, name='browse'),
    path('product/<int:id>', views.product_detail, name="product_detail"),
    path('', views.home, name='home'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    
]