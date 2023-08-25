from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:home")  
    else:
        form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"form":form})

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/accounts/profile/'

class LogoutView(auth_views.LogoutView):
    next_page = '/'
    

@login_required
def profile_page(request):
    return render(request, 'accounts/profile_page.html')