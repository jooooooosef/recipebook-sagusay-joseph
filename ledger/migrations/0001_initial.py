# Generated by Django 5.0.2 on 2024-03-02 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='ledger.ingredient')),
                ('quantity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quantity', to='ledger.ingredient')),
                ('recipe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='ledger.recipe')),
            ],
        ),
    ]