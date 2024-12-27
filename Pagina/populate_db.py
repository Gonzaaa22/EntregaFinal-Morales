import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pagina.settings')  
django.setup()

from app_coder.models import Categoria, Page

def populate():
    
    categorias = {
        'Remeras': 'Prendas de vestir superiores casuales.',
        'Buzos': 'Ropa abrigada ideal para el invierno.',
        'Pantalones': 'Prendas inferiores para diferentes ocasiones.',
    }

    for nombre, descripcion in categorias.items():
        categoria, created = Categoria.objects.get_or_create(nombre=nombre, descripcion=descripcion)
        if created:
            print(f'Categoría creada: {nombre}')
        else:
            print(f'Categoría ya existente: {nombre}')

    
    productos = [
        {
            'titulo': 'Remera Oversize',
            'descripcion': 'Una remera cómoda y moderna.',
            'contenido': '<p>Perfecta para cualquier ocasión.</p>',
            'precio': 1999.99,
            'categoria': 'Remeras',
        },
        {
            'titulo': 'Remera Básica',
            'descripcion': 'Remera simple, ideal para el uso diario.',
            'contenido': '<p>Disponible en varios colores.</p>',
            'precio': 1499.99,
            'categoria': 'Remeras',
        },
        {
            'titulo': 'Buzo Clásico',
            'descripcion': 'Un buzo abrigado y estiloso.',
            'contenido': '<p>Ideal para días fríos.</p>',
            'precio': 3999.99,
            'categoria': 'Buzos',
        },
        {
            'titulo': 'Buzo con Capucha',
            'descripcion': 'Buzo cómodo con capucha y bolsillo frontal.',
            'contenido': '<p>Perfecto para días casuales.</p>',
            'precio': 4499.99,
            'categoria': 'Buzos',
        },
        {
            'titulo': 'Pantalón Jogger',
            'descripcion': 'Un pantalón perfecto para el día a día.',
            'contenido': '<p>Combina estilo y comodidad.</p>',
            'precio': 2499.99,
            'categoria': 'Pantalones',
        },
    ]

    for prod in productos:
        categoria = Categoria.objects.get(nombre=prod['categoria'])
        page, created = Page.objects.get_or_create(
            titulo=prod['titulo'],
            descripcion=prod['descripcion'],
            contenido=prod['contenido'],
            precio=prod['precio'],
            categoria=categoria
        )
        if created:
            print(f'Producto creado: {prod["titulo"]}')
        else:
            print(f'Producto ya existente: {prod["titulo"]}')

if __name__ == '__main__':
    populate()
