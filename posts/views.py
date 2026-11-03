from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# 1. LISTAR POSTS (Read)
def lista_posts(request):
    # Trae todos los posts de la base de datos y los ordena del más nuevo al más viejo
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'posts/lista_posts.html', {'posts': posts})



# 2. DETALLE DE UN POST (Read)
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalle_post.html', {'post': post})

# 3. CREAR POST (Create)
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Crear'})

# 4. EDITAR POST (Update)
@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Editar'})

# 5. ELIMINAR POST (Delete)
@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
