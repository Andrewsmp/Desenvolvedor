from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dev/', include('dev.urls')),
    path('habilidade/', include('habilidades.urls')),
    path('', include('usuario.urls')),
    path('admin/', admin.site.urls),
]
