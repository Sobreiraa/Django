from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    
    context = {
       'recipes': recipes #[make_recipe() for _ in range(10)],
    } 
    return render(request, 'recipes/pages/home.html', context) # Retornando uma renderização de uma página html


def category(request, category_id):
    #recipes = Recipe.objects.filter(
        #category__id=category_id,
        #is_published = True
    #).order_by('-id')

    #if not recipes:
        #raise Http404('Not Found :(')
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published = True
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })

def recipes(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published = True)

    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context)
