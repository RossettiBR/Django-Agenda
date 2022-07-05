from .test_base_contato import ContatosTestBase
from django.urls import resolve, reverse
from contatos import views


class DetalheViewsTest(ContatosTestBase):
    def test_contato_detalhe_view_função_correta(self):
        view = resolve(reverse('contato:detalhe', kwargs={'contato_id': 1}))
        self.assertIs(view.func, views.detalhe, 1)

    def test_contato_detalhe_view_retorna_404_contato_não_existe(self):
        response = self.client.get(reverse('contato:detalhe', kwargs={'contato_id': 10000}))
        self.assertEqual(response.status_code, 404)

    def test_contato_detalhe_view_carrega_templates_corretos_do_contato(self):
        test_nome = 'Esta renderizando o detalhe do contato.'

        self.make_contato(nome=test_nome)
        response = self.client.get(reverse('contato:detalhe', kwargs={'contato_id': 1}))

        content = response.content.decode('utf-8')
        self.assertIn(test_nome, content)

    def test_contato_detalhe_view_template_não_carrega_contato_não_publicado(self):
        contato = self.make_contato(mostrar=False)

        response = self.client.get(reverse('contato:detalhe', kwargs={'contato_id': contato.id}))
        self.assertEqual(response.status_code, 404)
