from django.test import TestCase
from django.urls import reverse


class ContatoURLsTest(TestCase):
    def test_contato_home_esta_correto(self):
        url = reverse('contato:index')
        self.assertEqual(url, '/')

    def test_contato_busca_esta_correto(self):
        url = reverse('contato:busca')
        self.assertEqual(url, '/busca/')

    def test_contato_detalhe_esta_correto(self):
        url = reverse('contato:detalhe', kwargs={'contato_id': 1})
        self.assertEqual(url, '/1')
