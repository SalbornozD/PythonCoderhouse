from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Noticia(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    body = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')

    def __str__(self):
        return self.title

class NoticiaImage(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='noticiasImages/')

    def __str__(self):
        return f"Image for {self.noticia.title}"

class Decreto(models.Model):
    title = models.CharField(max_length=100)  # Título del decreto
    body = models.TextField()  # Contenido del decreto
    publication_date = models.DateTimeField(auto_now_add=True)  # Fecha de publicación

    def __str__(self):
        return f"Decreto {self.id}: {self.title}"