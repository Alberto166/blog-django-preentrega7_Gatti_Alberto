from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relación uno a uno con el usuario nativo de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(blank=True, null=True)
    link_web = models.URLField(blank=True, null=True)
    # Guardará las imágenes en la subcarpeta media/avatares/
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
