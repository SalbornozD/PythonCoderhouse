from django.urls import path
from .views import get_noticia

urlpatterns = [
    path('<int:noticia_id>/', get_noticia, name='get_blogs')
]