from django.shortcuts import render, redirect
from .models import *
from .forms import *
import datetime
from Users.forms import UserForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def inicio(request):

    return render(request, 'Blog/static/Blog/index.html')


@login_required
def crear_post(request):

    if request.method == 'POST':
        miForm = CrearPostFormulario(request.POST)
        user = request.user
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            post = Post (title = info['title'], date = datetime.datetime.now(), body = info['body'], tags = info['tags'], author = user)
            post.save()
            print(post.id)

            return redirect('../post_puntual/'+str(post.id),{ 'post_id': post.id})

    else:
        miForm = CrearPostFormulario()

    return render(request, 'Blog/templates/Blog/crear_post.html',{"miForm":miForm})

def posts(request):

    posts = Post.objects.all()

    return render(request, 'Blog/templates/Blog/posts.html', {'posts': posts})

def post_puntual(request, post_id):

    post = Post.objects.get(id = post_id)
    comments = Comments.objects.filter(post_id__icontains = post_id)

    print(comments)

    if request.method == 'POST':
        miForm2 = ComentarPosts(request.POST)
        user = request.user
        print(miForm2)
        if miForm2.is_valid:
            info = miForm2.cleaned_data

            comentario = Comments (user = user, body_comment = info['body_comment'], post_id = post.id)
            comentario.save()


            return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})

    else:
        miForm2 = ComentarPosts()

        return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})


    return render(request, 'Blog/templates/Blog/post_puntual.html', {'post':post, 'comments':comments})

def buscar_autor(request):

    return render(request, 'Blog/templates/Blog/buscar_por_autor.html')

def buscar(request):

    print("Hola", request.GET['author'])

    if request.GET['author']:

        author = request.GET['author']
        posts = Post.objects.filter(author__icontains=author)

        return render(request, "Blog/templates/Blog/resultados_busqueda.html", {"author":author, "posts":posts})
    
    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)




