from contatos import views
from django.urls import resolve, reverse
from .test_base_contato import ContatosTestBase


class BuscaViewsTest(ContatosTestBase):
    def test_contato_busca_view_função_esta_correta(self):
        view = resolve(reverse('contato:busca'))
        self.assertIs(view.func, views.busca)

    def test_contato_busca_view_carrega_template_correto(self):
        response = self.client.get(reverse('contato:busca') + '?termo=teste')
        self.assertTemplateUsed(response, 'contatos/busca.html')

    def test_contato_busca_view_carrega_termo_vazio(self):
        response = self.client.get(reverse('contato:busca'))
        self.assertEqual(response.status_code, 302)

    def test_contato_busca_view_busca_contato_pelo_nome(self):
        nome1 = 'Nome1'
        nome2 = 'Nome2'

        contato1 = self.make_contato(
            nome=nome1,
        )

        contato2 = self.make_contato(
            nome=nome2
        )

        busca_url = reverse('contato:busca')
        response1 = self.client.get(f'{busca_url}?termo={contato1}')
        response2 = self.client.get(f'{busca_url}?termo={contato2}')

        self.assertIn(contato1, response1.context['contatos'])
        self.assertNotIn(contato2, response1.context['contatos'])

        self.assertIn(contato2, response2.context['contatos'])
        self.assertNotIn(contato1, response2.context['contatos'])
