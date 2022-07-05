from django.urls import path
from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.detalhe, name='detalhe'),
]
