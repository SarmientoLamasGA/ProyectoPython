from django.shortcuts import render 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import UserProfile, Avatar
from .forms import UserForm, UserEditForm, AvatarUpload, ProfileForm

# Create your views here.

@login_required
def user(request):
    if request.method == "POST":
        form = AvatarUpload(request.POST, request.Files)
        if form.is_valid():
            form.save()
            image = form.instance
            return render(request, "user.html", {"url": image, "form": form})
    else:
        images = Avatar.objects.get(user=request.user)
        url = images.image.url
        form = AvatarUpload()
        return render(request, "user.html", {"url": url, "form": form})

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

def editUser(request):
    usuario = request.user

    if request.method == "POST":
        userForm = UserEditForm(request.POST)

        if userForm.is_valid():
            info = userForm.cleaned_data
            usuario.email = info['email'] 
            usuario.password1 = info['password1'] 
            usuario.password2 = info['password2']

            usuario.save()

            return render(request, "user.html")
    else:
        userForm = UserEditForm(initial=({"username": usuario.username, "email": usuario.email}))
    
    return render(request, "update.html", {"form": userForm, "usuario": usuario})
