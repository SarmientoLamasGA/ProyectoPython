from django.shortcuts import render, redirect
from .models import *
from .forms import *
import datetime

from django.http import HttpResponse


def inicio(request):

    return render(request, 'Blog/static/Blog/index.html')

def crear_post(request):

    if request.method == 'POST':
        miForm = CrearPostFormulario(request.POST)
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            post = Post (title = info['title'], date = datetime.datetime.now(), body = info['body'], tags = info['tags'], author = info['author'])
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
        print(miForm2)
        if miForm2.is_valid:
            info = miForm2.cleaned_data

            comentario = Comments (user = info['user'], body_comment = info['body_comment'], post_id = post.id)
            comentario.save()


            return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})

    else:
        miForm2 = ComentarPosts()

        return render(request, 'Blog/templates/Blog/post_puntual.html',{'post':post, "miForm2":miForm2, 'comments':comments})


    return render(request, 'Blog/templates/Blog/post_puntual.html', {'post':post, 'comments':comments})




