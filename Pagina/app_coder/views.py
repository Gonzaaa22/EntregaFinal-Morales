from django.shortcuts import render
from .models import Page

def home(request):
    pages = Page.objects.all()  # Obtener todas las páginas
    return render(request, 'home.html', {'pages': pages})  

def acerca_de(request):
    return render(request, 'acerca_de.html')

def lista_paginas(request):
    pages = Page.objects.all()  # Obtener todas las páginas 
    if pages.exists():
        return render(request, 'lista_paginas.html', {'pages': pages})
    else:
        return render(request, 'lista_paginas.html', {'mensaje': "No hay páginas aún"})

def detalle_pagina(request, id):
    pagina = Page.objects.get(id=id)  # Obtener la página específica
    return render(request, 'detalle_pagina.html', {'pagina': pagina})

from .forms import PageForm
from django.shortcuts import redirect

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

