from dev.views import ListViewDev, CreateViewDev, UpdateViewDev, DeleteviewDev
from django.urls import path

urlpatterns = [
    path('listar/', ListViewDev.as_view(), name='listar-dev'),
    path('inserir/', CreateViewDev.as_view(), name='inserir-dev'),
    path('alterar/<int:pk>/', UpdateViewDev.as_view(), name='alterar-dev'),
    path('deletar/<int:pk>/', DeleteviewDev.as_view(), name='deletar-dev')
]