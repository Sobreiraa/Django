from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


# Create your tests here.
class RecipeViewsTest(TestCase):
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
     
    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            is_published=True,
        )

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