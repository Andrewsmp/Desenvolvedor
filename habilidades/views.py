from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FrameWork, Linguagem

#Views de linguagem
class ListViewLing(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/listahab.html'
    queryset = Linguagem.objects.all()

    #Sobrescreve para informar qual contexto sera enviado para o template
    def get_context_data(self, **kwargs):
        context = super(ListViewLing, self).get_context_data(**kwargs)
        context['linguagens'] = Linguagem.objects.all()
        context['frameworks'] = FrameWork.objects.all()
        return context


class CreateViewLing(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuario:login')
    queryset = Linguagem.objects.all()
    fields = ['nome']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')


class UpdateViewLing(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuario:login')
    queryset = Linguagem.objects.all()
    fields = ['nome', 'ativo']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')


class DeleteviewLing(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')
    queryset = Linguagem.objects.all()

#Views de Framework

class CreateViewFrame(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuario:login')
    queryset = FrameWork.objects.all()
    fields = ['nome']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')


class UpdateViewFrame(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuario:login')
    queryset = FrameWork.objects.all()
    fields = ['nome', 'ativo']
    template_name = 'paginas/inserir.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')


class DeleteviewFrame(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuario:login')
    template_name = 'paginas/deletar.html'
    success_url = reverse_lazy('habilidades:listar-habilidade')
    queryset = FrameWork.objects.all()