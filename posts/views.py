from django.shortcuts import render
from .models import Post  

def inicio(request):
    return render(request, 'posts/inicio.html')

def acerca(request):
    return render(request, 'posts/acerca.html')

def lista_posts(request):
    # Traemos los posts filtrados desde la base de datos
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    
    context = {
        "posts": posts
    }
    # Renderizamos la plantilla enviándole el contexto
    return render(request, "posts/lista_posts.html", context)



