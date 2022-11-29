from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin): # Classe para as mostrar informações no admin do django
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin): # Classe para as mostrar informações no admin do django
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin) # Registrando os modelos
admin.site.register(Cliente, ClienteAdmin) # Registrando os modelos