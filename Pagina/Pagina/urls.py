from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_coder.urls')),  # Incluir rutas de la app_coder
    path('cuentas/', include('cuentas.urls')),  # Incluir rutas de la app_usuarios
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Aquí van tus otros path...
    path('', include('app_coder.urls')),  # Si tienes otros urlpatterns en tu app_coder
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
