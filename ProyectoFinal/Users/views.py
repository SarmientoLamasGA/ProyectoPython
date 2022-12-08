from django.shortcuts import render

from django.views.generic.detail import DetailView

# Create your views here.

class UserSection(DetailView):
    template_name= "user.html"

def user(request):
    return render(request, "user.html")

def login(request):
    pass

def register(request):
    pass