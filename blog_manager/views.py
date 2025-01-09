from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, NoticiaImage

def get_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    is_authenticated = request.user.is_authenticated  # Verificar si el usuario está autenticado

    # Pasar la noticia y el estado de autenticación al template
    return render(request, 'blog_manager/noticia.html', {'noticia': noticia, 'is_authenticated': is_authenticated})


@login_required
def create_noticia(request):
    data = {}
    if request.method == 'POST':
        # Obtencion de datos.
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        body = request.POST.get('body')
        categoria_id = request.POST.get('categoria')
        images = request.FILES.getlist('images')  

        # Validar campos obligatorios
        if not title or not body or not categoria_id:
            data['categorias'] = Categoria.objects.all()
            data['error_message'] = "Todos los campos obligatorios deben completarse."
            return render(request, 'blog_manager/form_noticia.html', data)

        # Crear la noticia
        noticia = Noticia(
            title=title,
            caption=caption,
            body=body,
            autor=request.user,
            categoria_id=categoria_id
        )
        noticia.save()

        # Asociar imágenes a la noticia
        for image in images:
            noticia_image = NoticiaImage(noticia=noticia, image=image)
            noticia_image.save()

        return redirect('index') 

    # Cargar categorías para el formulario
    data['categorias'] = Categoria.objects.all()
    return render(request, 'blog_manager/form_noticia.html', data)

@login_required
def edit_noticia(request, noticia_id):
    data = {}
    noticia = get_object_or_404(Noticia, id=noticia_id)
    data['noticia'] = noticia

    if request.method == 'POST':
        # Actualizar datos básicos de la noticia
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        body = request.POST.get('body')
        categoria_id = request.POST.get('categoria')
        images = request.FILES.getlist('images')

        # Validar campos obligatorios
        if not title or not body or not categoria_id:
            data['categorias'] = Categoria.objects.all()
            data['error_message'] = "Todos los campos obligatorios deben completarse."
            return render(request, 'blog_manager/form_noticia.html', data)

        # Actualizar campos de la noticia
        noticia.title = title
        noticia.caption = caption
        noticia.body = body
        noticia.categoria_id = categoria_id
        noticia.save()

        # Manejar imágenes: eliminar existentes si se suben nuevas
        if images:
            noticia.images.all().delete()  # Eliminar imágenes anteriores
            for image in images:
                noticia_image = NoticiaImage(noticia=noticia, image=image)
                noticia_image.save()

        return redirect('index')  # Redirigir a la página principal

    # Cargar categorías y datos para el formulario
    data['categorias'] = Categoria.objects.all()
    return render(request, 'blog_manager/form_noticia.html', data)

@login_required
def delete_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.delete()
    return redirect('index')