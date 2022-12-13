from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar, UserProfile

class UserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2"
        ]
        help_texts = {k: "" for k in fields}

class AvatarUpload(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ["image"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("name", "lastName", "author")
