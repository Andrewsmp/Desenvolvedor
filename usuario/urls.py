from django.urls import path
from django.contrib.auth import views as auth_view
from .views import CreateViewUsuario, ListViewUsuario, UpdateViewUsuario, DeleteViewUsuario

app_name = 'usuario'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(
        template_name = 'paginas/index.html'
    ), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('inserir/', CreateViewUsuario.as_view(), name='cadastrar'),
    path('listar/', ListViewUsuario.as_view(), name='listar'),
    path('alterar/<int:pk>/', UpdateViewUsuario.as_view(), name='alterar'),
    path('deletar/<int:pk>/', DeleteViewUsuario.as_view(), name='deletar'),
]