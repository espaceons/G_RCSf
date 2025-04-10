from django.urls import path
from . import views


app_name = 'cuisine'


urlpatterns = [
    path('plats/', views.liste_plats, name='liste_plats'),
    path('plats/ajouter/', views.ajouter_plat, name='ajouter_plat'),
    path('plats/modifier/<int:plat_id>/', views.modifier_plat, name='modifier_plat'),
    path('plats/supprimer/<int:plat_id>/', views.supprimer_plat, name='supprimer_plat'),
]