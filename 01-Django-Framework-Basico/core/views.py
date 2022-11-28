from django.shortcuts import render

# Create your views here.
def index(request): # Criando a view INDEX
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é incrível!'
    }
    return render(request, 'index.html', context)


def contact(request): # Criando a view CONTACT
    return render(request, 'contact.html')

