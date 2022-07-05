from unittest.mock import patch

from contatos import views
from django.urls import reverse, resolve

from .test_base_contato import ContatosTestBase


class ContatoViewsTest(ContatosTestBase):
    def test_contato_home_view_função_esta_correta(self):
        view = resolve(reverse('contato:index'))
        self.assertIs(view.func, views.index)

    def test_contato_home_views_esta_retornando_codigo_200(self):
        response = self.client.get(reverse('contato:index'))
        self.assertEqual(response.status_code, 200)

    def test_contato_home_views_esta_carregando_templates(self):
        response = self.client.get(reverse('contato:index'))
        self.assertTemplateUsed(response, 'contatos/index.html')

    def test_contato_home_views_esta_carregando_contatos(self):
        self.make_contato()

        response = self.client.get(reverse('contato:index'))
        content = response.content.decode('utf-8')
        response_context_contato = response.context['contatos']

        self.assertIn('Fulano', content)
        self.assertEqual(len(response_context_contato), 1)

    def test_contato_home_paginação(self):
        self.make_contato_in_varios(qtd=8)

        with patch('contatos.views.PER_PAGE', new=3):
            response = self.client.get(reverse('contato:index'))
            contatos = response.context['contatos']
            paginator = contatos.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)

    def test_invalido_page_query_usada_pagina_um(self):
        self.make_contato_in_varios(qtd=8)

        with patch('contatos.views.PER_PAGE', new=3):
            response = self.client.get(reverse('contato:index') + '?p=1')
            self.assertEqual(response.context['contatos'].number, 1)
