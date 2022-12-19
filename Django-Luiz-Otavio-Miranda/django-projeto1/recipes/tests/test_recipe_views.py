from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home')
            )
        self.assertIs(view.func, views.home) #Verificando se as duas funções são as mesmas
    
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
            )
        self.assertIs(view.func, views.category) #Verificando se as duas funções são as mesmas
    
    def test_recipe_details_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
            )
        self.assertIs(view.func, views.recipes)