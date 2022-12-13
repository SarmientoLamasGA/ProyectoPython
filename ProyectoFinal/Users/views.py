from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import UserProfile, Avatar
from .forms import UserForm, UserEditForm, AvatarUpload, ProfileForm

# Create your views here.

@login_required
def user(request):
    usuario = User.objects.get(id=request.user.pk)
    if request.method == "POST":
        form = AvatarUpload(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar.objects.get(user=usuario)
            avatar.image = form.cleaned_data["image"]
            avatar.save()
            return render(request, "user.html", {"url": avatar.image.url, "form": form})

    try:
        images = Avatar.objects.get(user_id=request.user.pk)
    except:
        images = Avatar.objects.create(user=usuario)
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

def editProfile(request):
    perfil = request.user.userprofile
    profileForm = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            perfil.name = info["name"]
            perfil.lastName = info["lastName"]
            perfil.author = info["author"]
            perfil.save()
            return render(request, "userInfo.html", {"form": profileForm})
        
    return render(request, "userInfo.html", {"form": profileForm})
