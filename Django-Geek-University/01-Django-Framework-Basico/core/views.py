from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

# Create your views here.
def index(request): # Criando a view INDEX

    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é incrível!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contact(request): # Criando a view CONTACT
    return render(request, 'contact.html')


def produto(request, pk): # Criando a view PRODUTO

    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type = 'text/html: charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type = 'text/html: charset=utf8', status=500)