# Aqui foi criado o arquivo URLS.py da aplicação, para usar as rotas da aplicação
from django.urls import path
from .views import index, contact # Importando as duas views criadas no arquivos views.py

urlpatterns = [
    path('', index),
    path('contact', contact), 
]