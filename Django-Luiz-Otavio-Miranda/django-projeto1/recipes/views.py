from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    context = {
        'name': 'Matheus Sobreira'
    } # Contexto que pode ser mandado para a função render
    return render(request, 'recipes/pages/home.html', context) # Retornando uma renderização de uma página html

