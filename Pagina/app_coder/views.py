from django.shortcuts import render
from .models import Page
from .forms import PageForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Page, CartItem

def home(request):
    pages = Page.objects.all()
    return render(request, 'home.html', {'pages': pages})

def acerca_de(request):
    return render(request, 'acerca_de.html')

from django.shortcuts import render
from app_coder.models import Page

def lista_paginas(request):
    categoria = request.GET.get('categoria') 
    if categoria:
        pages = Page.objects.filter(categoria__nombre=categoria)
    else:
        pages = Page.objects.all()
    return render(request, 'lista_paginas.html', {
        'pages': pages,
        'categoria_actual': categoria
    })



def detalle_pagina(request, id):
    pagina = Page.objects.get(id=id)
    return render(request, 'detalle_pagina.html', {'pagina': pagina})

def crear_pagina(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_paginas')
    else:
        form = PageForm()
    return render(request, 'formulario_pagina.html', {'form': form})

def editar_pagina(request, id):
    pagina = Page.objects.get(id=id)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=pagina)
        if form.is_valid():
            form.save()
            return redirect('lista_paginas')
    else:
        form = PageForm(instance=pagina)
    return render(request, 'formulario_pagina.html', {'form': form})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Page, id=producto_id)
    cart_item, created = CartItem.objects.get_or_create(
        usuario=request.user,
        producto=producto
    )
    if not created:
        cart_item.cantidad += 1
        cart_item.save()
    messages.success(request, f'{producto.titulo} agregado al carrito')
    return redirect('lista_paginas')

def ver_carrito(request):
    if request.user.is_authenticated:
        carrito = CartItem.objects.filter(usuario=request.user)
    else:
        carrito = []  # Si el usuario no está autenticado

    total = sum(item.total_price() for item in carrito)  # Calcula el total del carrito

    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, usuario=request.user)
    item.delete()
    messages.success(request, 'Producto eliminado del carrito')
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, usuario=request.user)
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    if nueva_cantidad > 0:
        item.cantidad = nueva_cantidad
        item.save()
    return redirect('ver_carrito')


from django.shortcuts import render
from .models import Page

def categoria_view(request, categoria):
    # Filtrar los productos por la categoría seleccionada
    productos = Page.objects.filter(categoria=categoria)
    
    return render(request, 'app_coder/categoria.html', {'productos': productos, 'categoria': categoria})
