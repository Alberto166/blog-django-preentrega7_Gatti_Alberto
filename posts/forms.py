from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Incluimos los campos requeridos en la consigna
        fields = ['titulo', 'contenido', 'autor', 'estado', 'imagen']
