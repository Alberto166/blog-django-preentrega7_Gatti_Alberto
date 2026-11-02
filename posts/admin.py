from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Esto define las columnas que vas a ver en el listado del panel
    list_display = ('titulo', 'autor', 'estado', 'fecha_creation_display')

    # Truco opcional para ver la fecha linda en el panel admin
    def fecha_creation_display(self, obj):
        return obj.fecha_creacion.strftime('%d/%m/%Y %H:%M')
    fecha_creation_display.short_description = 'Fecha de Creación'

# Registramos el modelo junto con su configuración personalizada
admin.site.register(Post, PostAdmin)
