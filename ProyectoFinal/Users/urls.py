from django.urls import path

from Users import views

urlpatterns = [
    path('', views.user, name="User Home"),
    path('register', views.register, name="Register"),
    path('login', views.UserLogin.as_view(), name="Login"),
    path('logout', views.UserLougout.as_view(), name="Logout"),
    path('update', views.editUser, name="Update")
]

