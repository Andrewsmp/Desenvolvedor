from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Desenvolvedor


class ListViewDev(ListView):
    template_name = 'paginas/listadev.html'
    queryset = Desenvolvedor.objects.all()


class CreateViewDev(CreateView):
    queryset = Desenvolvedor.objects.all()
    fields = ['nome', 'email', 'linguagem', 'framework']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('listar-dev')


class UpdateViewDev(UpdateView):
    queryset = Desenvolvedor.objects.all()
    fields = ['nome', 'email', 'linguagem', 'framework', 'ativo']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('listar-dev')


class DeleteviewDev(DeleteView):
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('listar-dev')
    queryset = Desenvolvedor.objects.all()