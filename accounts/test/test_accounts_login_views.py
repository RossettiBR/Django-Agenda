from unittest import TestCase
from parameterized import parameterized
from accounts.models import FormContato
from 

class LoginRegistroUnitestTest(TestCase):
    @parameterized.expand([
        ('username', 'usuario'),
        ('password', 'senha'),
    ])
    def test_login_views_metodo_get(self):
        User.ob
