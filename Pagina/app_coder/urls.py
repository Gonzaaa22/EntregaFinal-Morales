from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('páginas/', views.lista_paginas, name='lista_paginas'),
    path('páginas/<int:id>/', views.detalle_pagina, name='get_page'), 
    path('páginas/crear/', views.crear_pagina, name='crear_pagina'),
    path('páginas/editar/<int:id>/', views.editar_pagina, name='editar_pagina'),
]
