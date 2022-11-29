# Aqui foi criado o arquivo URLS.py da aplicação, para usar as rotas da aplicação
from django.urls import path
from .views import index, contact, produto # Importando as duas views criadas no arquivos views.py

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'), 
    path('produto/<int:pk>', produto, name='produto')
]