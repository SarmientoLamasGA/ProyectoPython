from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20, label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label='Repetir contraseña', widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    email = forms.EmailField(max_length=50)
    name = forms.CharField(max_length=40)
    lastName = forms.CharField(max_length=40)
    author = forms.BooleanField(label='¿Eres escritor?')
