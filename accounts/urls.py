from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('profile/', views.profile_page, name='profile_page'),
]