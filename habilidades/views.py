from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import FrameWork, Linguagem


class ListViewHab(ListView):
    template_name = 'paginas/listahab.html'
    queryset = Linguagem.objects.all()


class CreateViewHab(CreateView):
    queryset = Linguagem.objects.all()
    fields = ['nome']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('listar-habilidade')


class UpdateViewHab(UpdateView):
    queryset = Linguagem.objects.all()
    fields = ['nome', 'ativo']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('listar-habilidade')


class DeleteviewHab(DeleteView):
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('listar-habilidade')
    queryset = Linguagem.objects.all()