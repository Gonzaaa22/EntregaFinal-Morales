from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='imagenes_pagina/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
