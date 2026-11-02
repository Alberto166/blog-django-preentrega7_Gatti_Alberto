from django.shortcuts import render

def inicio(request):
    # El render busca automáticamente adentro de la carpeta templates/
    return render(request, 'posts/inicio.html')

def acerca(request):
    return render(request, 'posts/acerca.html')

