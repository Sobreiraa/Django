from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin) # 2° forma de registrar models


@admin.register(Recipe) # 1° forma de registrar models
class RecipeAdmin(admin.ModelAdmin):
    ...