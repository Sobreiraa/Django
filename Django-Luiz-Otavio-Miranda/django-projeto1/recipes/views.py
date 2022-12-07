from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    context = {
       'recipes': [make_recipe() for _ in range(10)],
    } 
    return render(request, 'recipes/pages/home.html', context) # Retornando uma renderização de uma página html


def recipes(request, id):
    context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context)
