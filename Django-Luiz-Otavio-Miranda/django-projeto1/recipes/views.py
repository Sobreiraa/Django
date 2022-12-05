from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    return HttpResponse('Home') # Retornando um HTTP RESPONSE


def contato(request): #HTTP REQUEST
    # HTTP RESPONSE
    return HttpResponse('Contato') # Retornando um HTTP RESPONSE


def sobre(request): #HTTP REQUEST
    # HTTP RESPONSE
    return HttpResponse('Sobre') # Retornando um HTTP RESPONSE