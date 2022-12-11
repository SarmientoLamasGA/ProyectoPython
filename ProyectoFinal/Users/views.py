from django.shortcuts import render 
from django.contrib.auth.views import LoginView, LogoutView

from .models import UserProfile, Avatar
from .forms import UserForm, UserEditForm, ProfileForm

# Create your views here.
