from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Page(models.Model):
    CATEGORIA_CHOICES = [
        ('pantalones', 'Pantalones'),
        ('buzos', 'Buzos'),
        ('remeras', 'Remeras'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_pagina/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo

class CartItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Page, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.producto.titulo} - {self.cantidad}'

    def total_price(self):
        return self.cantidad * self.producto.precio
