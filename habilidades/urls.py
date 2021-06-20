from .views import ListViewLing, CreateViewLing, UpdateViewLing, DeleteviewLing
from .views import CreateViewFrame, UpdateViewFrame, DeleteviewFrame
from django.urls import path

app_name = 'habilidades'

urlpatterns = [
    #Urls de linguagem
    path('listar/', ListViewLing.as_view(), name='listar-habilidade'),
    path('inserir/linguagem/', CreateViewLing.as_view(), name='inserir-linguagem'),
    path('alterar/linguagem/<int:pk>/', UpdateViewLing.as_view(), name='alterar-linguagem'),
    path('deletar/linguagem/<int:pk>/', DeleteviewLing.as_view(), name='deletar-linguagem'),
    #Urls de Framework
    path('inserir/framework/', CreateViewFrame.as_view(), name='inserir-framework'),
    path('alterar/framework/<int:pk>/', UpdateViewFrame.as_view(), name='alterar-framework'),
    path('deletar/framework/<int:pk>/', DeleteviewFrame.as_view(), name='deletar-framework'),
]