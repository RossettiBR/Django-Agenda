from django.test import TestCase
from django.urls import reverse


class AccountsURLsTest(TestCase):
    def test_account_url_esta_correto(self):
        url = reverse('account:index_login')
        self.assertEqual(url, '/accounts/')

    def test_account_login_url_esta_correta(self):
        url = reverse('account:login')
        self.assertEqual(url, '/accounts/login/')

    def test_account_logout_url_esta_correta(self):
        url = reverse('account:logout')
        self.assertEqual(url, '/accounts/logout/')

    def test_account_cadastro_url_esta_correta(self):
        url = reverse('account:cadastro')
        self.assertEqual(url, '/accounts/cadastro/')

    def test_account_dashboard_url_esta_correta(self):
        url = reverse('account:dashboard')
        self.assertEqual(url, '/accounts/dashboard/')
