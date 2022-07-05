from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Contato(models.Model):
    nome = models.CharField(max_length=65)
    sobrenome = models.CharField(max_length=65,  blank=True)
    telefone = models.CharField(max_length=65)
    email = models.EmailField(max_length=65, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self) -> str:
        return self.nome
