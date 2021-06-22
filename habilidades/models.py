from django.db import models


class Base(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_modificacao = models.DateTimeField('Data de modificação', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Linguagem(Base):
    nome = models.CharField('Nome', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Linguagem'
        verbose_name_plural = 'Linguagens'

    def __str__(self):
        return self.nome



class FrameWork(Base):
    nome = models.CharField('Nome', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Framework'
        verbose_name_plural = 'Frameworks'

    def __str__(self):
        return self.nome       