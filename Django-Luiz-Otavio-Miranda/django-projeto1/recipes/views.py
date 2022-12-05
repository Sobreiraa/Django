from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    context = {
        'name': 'Matheus Sobreira'
    } # Contexto que pode ser mandado para a função render
    return render(request, 'recipes/home.html', context) # Retornando uma renderização de uma página html


def contato(request): #HTTP REQUEST
    # HTTP RESPONSE
    return HttpResponse('Contato') # Retornando um HTTP RESPONSE


def sobre(request): #HTTP REQUEST
    # HTTP RESPONSE
    return HttpResponse('Sobre') # Retornando um HTTP RESPONSE