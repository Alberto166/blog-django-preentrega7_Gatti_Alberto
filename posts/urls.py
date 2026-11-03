from django.urls import path
from . import views


urlpatterns = [
    # Ruta principal para listar todos los posts
    path('', views.lista_posts, name='lista_posts'),
    
    # Ruta para ver el detalle de un post específico usando su ID (pk)
    path('posts/<int:pk>/', views.detalle_post, name='detalle_post'),
    
    # Ruta para el formulario de creación
    path('posts/crear/', views.crear_post, name='crear_post'),
    
    # Ruta para editar un post específico
    path('posts/<int:pk>/editar/', views.editar_post, name='editar_post'),
    
    # Ruta para eliminar un post con confirmación
    path('posts/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
]


