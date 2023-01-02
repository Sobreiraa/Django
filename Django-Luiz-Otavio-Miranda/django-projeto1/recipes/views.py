from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from recipes.models import Recipe
from django.http import Http404
from utils.pagination import make_pagination_range

# Create your views here.
def home(request): #HTTP REQUEST
    # HTTP RESPONSE
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
        
    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
    )
    
    context = {
       'recipes': page_obj,
       'pagination_range': pagination_range
    } 
    return render(request, 'recipes/pages/home.html', context) 

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


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
       title__icontains=search_term,
       is_published=True,
    ).order_by('-id')



    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for {search_term} |',
        'recipes': recipes,
    })
