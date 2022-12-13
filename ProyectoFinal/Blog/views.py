from django.shortcuts import render, redirect
from .models import *
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def inicio(request):

    return render(request, 'static/Blog/index.html')


@login_required
def crear_post(request):

    if request.method == 'POST':
        miForm = CrearPostFormulario(request.POST)
        user = request.user
        if miForm.is_valid():
            info = miForm.cleaned_data
            image = request.FILES.get('image')
            post = Post (
                title = info['title'], 
                date = datetime.datetime.now(), 
                body = info['body'], 
                tags = info['tags'], 
                author = user, 
                image = image
            )
            post.save()
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

    if request.method == 'POST':

        miForm2 = ComentarPosts(request.POST)
        user = request.user
        print(miForm2)

        if miForm2.is_valid:

            info = miForm2.cleaned_data
            comentario = Comments (
            user = user, 
            body_comment = info['body_comment'], 
            post_id = post.id
            )
            comentario.save()

            return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})

    else:
        miForm2 = ComentarPosts()

        return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})


    return render(request, 'Blog/templates/Blog/post_puntual.html', {'post':post, 'comments':comments})


@login_required
def borrar_post(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('../../posts/')

@login_required
def modificar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if image:
            post.image = image
        
        post.title = data.get("title")
        post.date = datetime.datetime.now()
        post.body = data.get("body")
        post.tags = data.get("tags")
        
        post.save()
        return redirect('../post_puntual/'+str(post.id))

    else: 
        miForm = CrearPostFormulario(initial={
        "title": post.title,
        "date": post.date,
        "body": post.body,
        "tags": post.tags,
        "author": post.author,
        "image": post.image,
        })

    return render(request, "Blog/templates/Blog/modificar_post.html", {"miForm":miForm})

@login_required
def borrar_comentario(request, post_id, comment_id):

    post = post_id
    comment = Comments.objects.get(id=comment_id)
    comment.delete()

    return redirect('../../post_puntual/'+str(post),{ 'post': post})

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





