from django.shortcuts import render
from .models import *
#from .forms import *

from django.http import HttpResponse


def inicio(request):

    return render(request, 'Blog/static/Blog/index.html')