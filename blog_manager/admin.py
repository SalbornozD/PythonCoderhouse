from django.contrib import admin
from .models import Noticia, NoticiaImage, Categoria, Decreto

# Register your models here.

admin.site.register(Noticia)
admin.site.register(NoticiaImage)
admin.site.register(Categoria)
admin.site.register(Decreto)