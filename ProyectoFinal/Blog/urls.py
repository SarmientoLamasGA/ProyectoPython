from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('posts/', views.posts, name = "Lista de posts"),
    path('crear_post/', views.crear_post, name = "Crear post"),
    path('post_puntual/<post_id>', views.post_puntual, name = "Post puntual"),

]