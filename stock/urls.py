from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    # Exemple : Liste des ingrédients
    path('ingredients/', views.liste_ingredients, name='liste_ingredients'),

    # Exemple : Ajouter un nouvel ingrédient
    path('ingredients/ajouter/', views.ajouter_ingredient, name='ajouter_ingredient'),

    # Exemple : Modifier un ingrédient existant
    path('ingredients/modifier/<int:ingredient_id>/', views.modifier_ingredient, name='modifier_ingredient'),

    # Exemple : Supprimer un ingrédient
    path('ingredients/supprimer/<int:ingredient_id>/', views.supprimer_ingredient, name='supprimer_ingredient'),

    # Exemple : Liste des fournisseurs
    path('fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),

    # Exemple : Ajouter un nouveau fournisseur
    path('fournisseurs/ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),

    # Exemple : Modifier un fournisseur existant
    path('fournisseurs/modifier/<int:fournisseur_id>/', views.modifier_fournisseur, name='modifier_fournisseur'),

    # Exemple : Supprimer un fournisseur
    path('fournisseurs/supprimer/<int:fournisseur_id>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
]