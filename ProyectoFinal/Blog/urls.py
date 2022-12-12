from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('posts/', views.posts, name = "Lista de posts"),
    path('crear_post/', views.crear_post, name = "Crear post"),
    path('post_puntual/<post_id>', views.post_puntual, name = "Post puntual"),
    path('buscar_autor/', views.buscar_autor, name = "Buscar autor"),
    path('buscar/', views.buscar),
    path('borrar_comentario/<post_id>/<comment_id>', views.borrar_comentario, name="Eliminar comentario"),
    path('borrar_post/<post_id>', views.borrar_post, name="Eliminar post"),
    path('modificar_post/<post_id>', views.modificar_post, name="Editar post")
]