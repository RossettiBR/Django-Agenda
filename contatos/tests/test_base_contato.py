from django.test import TestCase
from contatos.models import Contato, Categoria


class ContatoMixin:
    def make_categoria(self, name='Categoria'):
        return Categoria.objects.create(name=name)

    def make_contato(
        self,
        categoria=None,
        nome='Fulano',
        sobrenome='Raiz',
        telefone='123456789',
        email='fulano@email.com',
        descricao='Teste contato',
        mostrar=True,
    ):

        if categoria is None:
            categoria = {}

        return Contato.objects.create(
            categoria=self.make_categoria(**categoria),
            nome=nome,
            sobrenome=sobrenome,
            telefone=telefone,
            email=email,
            descricao=descricao,
            mostrar=mostrar,
        )

    def make_contato_in_varios(self, qtd=10):
        contatos = []
        for i in range(qtd):
            kwargs = {
                'nome': f'Fulano Nome {i}',
                'telefone': f'123456890{i}',
            }
            contato = self.make_contato(**kwargs)
            contatos.append(contato)


class ContatosTestBase(TestCase, ContatoMixin):
    def setUp(self) -> None:
        return super().setUp()
