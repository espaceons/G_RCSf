from django.shortcuts import render


def dashboard(request):
    context = {
        'applications': [
            {'name': 'Foyer', 'url': 'foyer:sous_dashboard_foyer', 'description': 'Gérer les événements et réservations.'},
            {'name': 'Stock', 'url': 'stock:liste_ingredients', 'description': 'Gérer les ingrédients et fournisseurs.'},
            {'name': 'Cuisine', 'url': 'cuisine:liste_plats', 'description': 'Gérer les recettes et menus.'},
            {'name': 'Authentification', 'url': 'comptes:login', 'description': 'Se connecter ou s\'inscrire.'},
        ]
    }
    return render(request, 'dashboard.html', context)