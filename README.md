# Blog Django

Proyecto de un blog web desarrollado con Django para la Preentrega 8 y Preentrega 9 y preentrega 10 y preentrega 11

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

##  Preentrega 10: CRUD de Posts con Imágenes en Django

Este módulo añade un sistema de gestión CRUD dinámico que permite administrar las publicaciones directamente desde la interfaz web del blog, incorporando además soporte para la carga y visualización de archivos multimedia (imágenes).

###  Nueva Dependencia Instalada
* **Pillow**: Librería fundamental para el procesamiento y validación del campo `ImageField` en los modelos de Django.

###  Configuración Multimedia (Media Files)
1. Se definieron `MEDIA_URL = '/media/'` y `MEDIA_ROOT = BASE_DIR / 'media'` en `settings.py`.
2. Se modificó el archivo `blog_project/urls.py` incorporando `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` de forma condicional (`if settings.DEBUG`) para servir de forma segura los archivos en el entorno de desarrollo.
3. Se implementó el atributo obligatorio `enctype="multipart/form-data"` en el formulario HTML para habilitar la transferencia binaria de archivos hacia el servidor.

###  Operaciones CRUD Disponibles
* **Listar (Read)**: Despliegue general en la ruta raíz `/`.
* **Detalle (Read)**: Vista individual en `/posts/<id>/` que valida la existencia de imágenes mediante `{% if post.imagen %}`.
* **Crear (Create)**: Formulario de alta en `/posts/crear/` procesando `request.FILES`.
* **Editar (Update)**: Modificación de campos y reemplazo de archivos en `/posts/<id>/editar/`.
* **Eliminar (Delete)**: Remoción física previa confirmación explícita del usuario en `/posts/<id>/eliminar/`.

###  Pruebas Automatizadas (Tests)
* Se añadió una prueba en `posts/tests.py` que valida el correcto filtrado del ORM para publicaciones en estado 'publicado'.
* Se puede ejecutar mediante el comando: `python manage.py test`

##  Preentrega  11: Autenticación, Usuarios y Perfiles

En esta preentrega se incorporó un sistema de gestión de usuarios y perfiles al Blog.

###  Funcionalidades Incluidas:
* **Registro de Usuarios:** Formulario personalizado basado en `UserCreationForm` para dar de alta nuevas cuentas.
* **Autenticación Completa:** Vistas integradas para el Inicio de Sesión (`LoginView`) y Cierre de Sesión (`LogoutView`).
* **Modelo Perfil:** Extensión de datos de usuario mediante una relación `OneToOneField` con campos para Biografía, Sitio Web y Avatar (Imagen).
* **Protección de Rutas:** Implementación del decorador `@login_required` para bloquear la creación, edición y eliminación de posts a usuarios que no hayan iniciado sesión.
* **Navegación Dinámica:** Menú adaptativo en `base.html` que varía según el estado de autenticación del usuario.

###  Cómo ejecutar las Migraciones:
Si es la primera vez que clonás el proyecto o querés impactar los cambios del perfil, ejecutá:
```shell
python manage.py makemigrations
python manage.py migrate
```
