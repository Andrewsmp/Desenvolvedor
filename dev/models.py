from django.db import models
from habilidades.models import Base, FrameWork, Linguagem


class Desenvolvedor(Base):
    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('E-mail', unique=True)
    linguagem = models.ManyToManyField(Linguagem)
    framework = models.ManyToManyField(FrameWork)

    class Meta:
        verbose_name = 'Desenvolvedor'
        verbose_name_plural = 'Desenvolvedores'

    def __str__(self):
        return self.nome