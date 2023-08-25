from django.urls import path
from . import views
from .views import wishlist_view, add_to_wishlist

app_name = "wishlist"

urlpatterns = [
    path('', wishlist_view, name='wishlist_view'),
    path('add_to_wishlist/<int:game_id>', add_to_wishlist, name='add_to_wishlist'),
    path('delete/<game_id>/', views.delete_from_wishlist, name='delete_from_wishlist'),
]