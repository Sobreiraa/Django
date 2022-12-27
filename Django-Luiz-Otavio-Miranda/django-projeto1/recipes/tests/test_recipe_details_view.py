from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


# Create your tests here.
class RecipeDetailsViewTest(TestCase): 
#---------------------TESTES DOS DETALHES------------------------
    def test_recipe_details_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
            )
        self.assertIs(view.func, views.recipes)
    
    def test_recipe_detail_view_return_404_if_no_recipes_found(self): # Teste 404 
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
    
    