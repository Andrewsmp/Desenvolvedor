from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User


class ListViewUsuario(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/listausuario.html'
    queryset = User.objects.all()


class CreateViewUsuario(LoginRequiredMixin, CreateView):
    queryset = User.objects.all()
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('usuario:listar')


class UpdateViewUsuario(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuario:login')
    queryset = User.objects.all()
    fields = ['username', 'email', 'first_name', 'last_name', 'is_active']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('usuario:listar')


class DeleteViewUsuario(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('usuario:listar')
    queryset = User.objects.all()
