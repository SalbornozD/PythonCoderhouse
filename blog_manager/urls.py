from django.urls import path
from .views import get_noticia, create_noticia, edit_noticia, delete_noticia

urlpatterns = [
    path('<int:noticia_id>/', get_noticia, name='get_blogs'),
    path('crear/', create_noticia, name='create_noticia'),
    path('editar/<int:noticia_id>/', edit_noticia, name='edit_noticia'),
    path('eliminar/<int:noticia_id>/', delete_noticia, name='delete_noticia')
]