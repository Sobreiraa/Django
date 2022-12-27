from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


# Create your tests here.
class RecipeHomeViewsTest(TestCase):
    #---------------------TESTES DA HOME---------------------
    def test_recipe_home_view_function_is_correct(self): # Testando se a view está correta
        view = resolve(
            reverse('recipes:home')
            )
        self.assertIs(view.func, views.home) #Verificando se as duas funções são as mesmas
    
    def test_recipe_home_view_return_status_code_200_OK(self): # Testando o código de resposta
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_correct_template(self): # Testando o template
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self): # Teste 404
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')
        )   

    