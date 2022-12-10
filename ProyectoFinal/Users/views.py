from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from .models import UserProfile
from .forms import UserForm, ProfileForm

# Create your views here.

def user(request):
    return render(request, "user.html")

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "user.html", {"form": form})
    
    else:
        form = UserForm()
    return render(request, "register.html", {"form": form})

class UserLogin(LoginView):
    template_name = "login.html"

class UserLougout(LogoutView):
    template_name = "logout.html"
