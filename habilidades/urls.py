from .views import ListViewHab, CreateViewHab, UpdateViewHab, DeleteviewHab
from django.urls import path

urlpatterns = [
    path('listar/', ListViewHab.as_view(), name='listar-habilidade'),
    path('inserir/', CreateViewHab.as_view(), name='inserir-habilidade'),
    path('alterar/<int:pk>/', UpdateViewHab.as_view(), name='alterar-habilidade'),
    path('deletar/<int:pk>/', DeleteviewHab.as_view(), name='deletar-habilidade')
]