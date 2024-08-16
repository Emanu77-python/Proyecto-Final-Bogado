from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
