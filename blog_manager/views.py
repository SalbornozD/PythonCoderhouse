from django.shortcuts import render, get_object_or_404
from .models import Noticia

def get_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    is_authenticated = request.user.is_authenticated  # Verificar si el usuario está autenticado

    # Pasar la noticia y el estado de autenticación al template
    return render(request, 'blog_manager/noticia.html', {'noticia': noticia, 'is_authenticated': is_authenticated})
