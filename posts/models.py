from django.db import models

class Post(models.Model):
    # Opciones predefinidas para el campo estado
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se guarda sola al crear el post
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='borrador')

    # NUEVO CAMPO:
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    # Método para que en el panel admin se vea el título del post en vez de "Post object (1)"
    def __str__(self):
        return self.titulo

