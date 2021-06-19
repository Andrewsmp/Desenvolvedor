from django.contrib import admin

from .models import Desenvolvedor
from habilidades.models import Linguagem, FrameWork


@admin.register(Desenvolvedor)
class DevAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'email',
        'data_criacao', 
        'data_modificacao', 
        'ativo'
        ]
    list_editable = ['ativo']


@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_modificacao', 'ativo']
    list_editable = ['ativo']


@admin.register(FrameWork)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_modificacao', 'ativo']
    list_editable = ['ativo']
