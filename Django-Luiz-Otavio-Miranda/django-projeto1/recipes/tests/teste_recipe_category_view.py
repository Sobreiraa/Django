from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


# Create your tests here.
class RecipeCategoryViewTest(TestCase):
    #---------------------TESTES DA CATEGORY---------------------
    def test_recipe_category_view_function_is_correct(self): # Testando se a view está correta
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
            )
        self.assertIs(view.func, views.category) #Verificando se as duas funções são as mesmas
    
    def test_recipe_category_view_return_404_if_no_recipes_found(self): #Teste 404
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 10000})
        )
        self.assertEqual(response.status_code, 404)
    
