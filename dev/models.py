from django.db import models
from habilidades.models import Base, FrameWork, Linguagem
from django.forms import ModelForm


class Desenvolvedor(Base):
    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('E-mail')
    linguagem = models.ManyToManyField(Linguagem)
    framework = models.ManyToManyField(FrameWork)

    class Meta:
        verbose_name = 'Desenvolvedor'
        verbose_name_plural = 'Desenvolvedores'


class DevForm(ModelForm):

    class Meta:
        model = Desenvolvedor
        fields = ['nome', 'email', 'linguagem', 'framework']
