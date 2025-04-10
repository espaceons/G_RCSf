from django.shortcuts import get_object_or_404, redirect, render
from .models import Ingredient
from .forms import IngredientForm


def liste_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'stock/liste_ingredients.html', {'ingredients': ingredients})


def ajouter_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:liste_ingredients')
    else:
        form = IngredientForm()
    return render(request, 'stock/ajouter_ingredient.html', {'form': form})

def modifier_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('stock:liste_ingredients')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'stock/modifier_ingredient.html', {'form': form})

def supprimer_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('stock:liste_ingredients')
    return render(request, 'stock/supprimer_ingredient.html', {'ingredient': ingredient})









from .forms import FournisseurForm
from .models import Fournisseur

def modifier_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, id=fournisseur_id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'stock/modifier_fournisseur.html', {'form': form})


def supprimer_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, id=fournisseur_id)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    return render(request, 'stock/supprimer_fournisseur.html', {'fournisseur': fournisseur})


def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'stock/liste_fournisseurs.html', {'fournisseurs': fournisseurs})

def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'stock/ajouter_fournisseur.html', {'form': form})