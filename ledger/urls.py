from django.contrib import admin
from django.urls import path, include
from .views import recipe_list, recipe_one, recipe_two

urlpatterns = [
    path('/recipes/list', recipe_list, name="recipe_list"),
    path('/recipe/1', recipe_one, name="recipe_one"),
    path('/recipe/2', recipe_two, name="recipe_one"),
]