from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # Creamos un post publicado y uno en borrador
        Post.objects.create(titulo="Post Publicado", contenido="Contenido", autor="Beto", estado="publicado")
        Post.objects.create(titulo="Post Borrador", contenido="Contenido", autor="Beto", estado="borrador")

    def test_filtro_posts_publicados(self):
        """Valida que solo se obtengan los posts con estado 'publicado'"""
        posts_publicados = Post.objects.filter(estado='publicado')
        self.assertEqual(posts_publicados.count(), 1)
        self.assertEqual(posts_publicados.first().titulo, "Post Publicado")

