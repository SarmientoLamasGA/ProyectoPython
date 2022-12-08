from django.urls import path

from Users import views

urlpatterns = [
    path('', views.user),
    path('login', views.login),
    path('register', views.register),
]