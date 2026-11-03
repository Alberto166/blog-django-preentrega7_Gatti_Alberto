# Blog Django

Proyecto de un blog web desarrollado con Django para la Preentrega 8 y Preentrega 9

## Descripción
Este repositorio contiene la estructura visual inicial del blog. A partir de la base anterior, se implementó el flujo completo de Django (Ruta -> Vista -> Template -> Estático) incorporando una plantilla base reutilizable (`base.html`), herencia de plantillas, un menú de navegación funcional y diseño con estilos CSS personalizados.

## Páginas Incluidas
* **Inicio**: Pantalla de bienvenida con la descripción general del proyecto.
* **Acerca de**: Sección interactiva con información del autor y el propósito del sitio.

## Requisitos Previos
* Python 3.x instalado.

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone URL_DEL_REPOSITORIO
   ```

2. **Entrar a la carpeta del proyecto:**
   ```bash
   cd blog_django
   ```

3. **Crear el entorno virtual:**
   ```bash
   python -m venv venv
   ```

4. **Activar el entorno virtual:**
   * En Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * En Linux o macOS:
     ```bash
     source venv/bin/activate
     ```

5. **Instalar las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

7. **Acceder desde el navegador:**
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Preentrega 9: Modelos y Admin configurados

En esta entrega se conectó la aplicación con una base de datos SQLite utilizando el ORM de Django, permitiendo la carga dinámica de publicaciones.

### Nuevas Funcionalidades
* **Modelo Post:** Definido en `posts/models.py` con campos para título, contenido, autor, fecha de creación y estado (Borrador/Publicado/Archivado).
* **Panel de Administración:** Modelo registrado en `posts/admin.py` con columnas personalizadas para una mejor gestión de los contenidos.
* **ORM & Plantillas Dinámicas:** La vista `lista_posts` filtra las publicaciones en estado "Publicado" y las renderiza dinámicamente mediante bucles en el HTML.


