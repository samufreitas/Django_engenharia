from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Local(models.Model):
    nome = models.CharField(max_length=255, null=True)
    rua = models.CharField(max_length=255, null=True)
    numero = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} da rua {self.rua}'

    class Meta:
        verbose_name_plural = 'Locais'


class Convidado(models.Model):
    nome = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'

    class Meta:
        verbose_name_plural = "Convidados"


class Agenda(models.Model):
    compromisso = models.CharField(max_length=255)
    data_inicio = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Convidado)

    def __str__(self):
        return f'{self.compromisso} começa {self.data_inicio} até {self.data_fim}'


# ----------------- Parte de teste -------------

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
