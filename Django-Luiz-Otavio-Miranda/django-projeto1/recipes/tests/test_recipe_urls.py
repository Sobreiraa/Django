from django.test import TestCase
from django.urls import reverse


class RecipeUrlsTest(TestCase):
    #---------------------TESTES DA HOME---------------------
    def test_recipe_home_url_is_correct(self): 
        url = reverse('recipes:home')
        self.assertEqual(url, '/') # se a home_url está resolvendo para '/'
    
    #---------------------TESTES DA CATEGORY---------------------
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')
    
    #---------------------TESTES DE DETAILS---------------------
    def test_recipe_details_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id':1})
        self.assertEqual(url, '/recipes/1/')