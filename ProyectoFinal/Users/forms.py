from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
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

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=40)
    lastName = forms.CharField(max_length=40)
    author = forms.BooleanField(label='¿Eres escritor?')
