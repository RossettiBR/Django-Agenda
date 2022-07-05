from django.core.exceptions import ValidationError
from parameterized import parameterized

from . test_base_contato import ContatosTestBase, Contato


class ContatoModelTest(ContatosTestBase):
    def setUp(self) -> None:
        self.contato = self.make_contato()
        return super().setUp()

    def make_contato_default(self):
        contato = Contato(
            categoria=self.make_categoria(name='Teste default contato'),
            nome='Fulano',
            sobrenome='Bunda',
            telefone='123456789',
            email='fulano@email.com',
            descricao='Fulano teste',
        )
        contato.full_clean()
        contato.save()
        return contato

    @parameterized.expand([
        ('nome', 65),
        ('sobrenome', 65),
        ('telefone', 65),
        ('email', 65)
    ])
    def test_contato_models_max_lenght(self, field, max_length):
        setattr(self.contato, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.contato.full_clean()

    def test_contato_models_mostrar_true_default(self):
        contato = self.make_contato_default()
        self.assertTrue(contato.mostrar)

    def test_contato_models_string_representação(self):
        needed = 'Fulano2'
        self.contato.nome = needed
        self.contato.full_clean()
        self.contato.save()
        self.assertEqual(
            str(self.contato), needed,
        )