from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Desenvolvedor


#Herda de ListView para renderizar um template de listagem
class ListViewDev(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/listadev.html'
    queryset = Desenvolvedor.objects.all()


class CreateViewDev(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuario:login')
    queryset = Desenvolvedor.objects.all()
    #Sobrescreve fields para carregar os campos no formulário
    fields = ['nome', 'email', 'linguagem', 'framework']
    #Sobrescreve template_name para renderizar um template
    template_name = 'paginas/inserir.html'
    #Succes_url diz para qual template renderizar e reverse_url retorna uma url
    success_url = reverse_lazy('dev:listar-dev')


class UpdateViewDev(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuario:login')
    queryset = Desenvolvedor.objects.all()
    fields = ['nome', 'email', 'linguagem', 'framework', 'ativo']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('dev:listar-dev')


class DeleteviewDev(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('dev:listar-dev')
    queryset = Desenvolvedor.objects.all()