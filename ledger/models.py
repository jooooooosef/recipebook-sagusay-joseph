from django.db import models

from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient", args=[self.name])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        "Ingredient", on_delete=models.CASCADE, related_name="recipe", default=1
    )
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name="ingredients", default=1
    )
