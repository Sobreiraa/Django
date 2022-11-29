from django.db import models

# Create your models here.
class Produto(models.Model): # Models que são classes em python
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self) -> str: # Método STR para ser apresentado de acordo com o que queremos
        return self.nome.title()


class Cliente(models.Model): # Models que são classes em python
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self) -> str: # Método STR para ser apresentado de acordo com o que queremos
        return f'{self.nome} {self.sobrenome}'.title()