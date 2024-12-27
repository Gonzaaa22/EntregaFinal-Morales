from django.urls import path
from . import views

urlpatterns = [
    # Tus URLs actuales
    path('', views.home, name='home'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('páginas/', views.lista_paginas, name='lista_paginas'),
    path('páginas/<int:id>/', views.detalle_pagina, name='get_page'),
    path('páginas/crear/', views.crear_pagina, name='crear_pagina'),
    path('páginas/editar/<int:id>/', views.editar_pagina, name='editar_pagina'),
    path('categoria/<str:categoria>/', views.categoria_view, name='categoria_view'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]