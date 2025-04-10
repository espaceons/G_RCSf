from django.urls import path
from . import views

app_name = 'foyer'


urlpatterns = [
    # Sous-dashboard de Foyer
    path('', views.sous_dashboard_foyer, name='sous_dashboard_foyer'),
    # Gestion des événements
    path('evenements/', views.liste_evenements, name='liste_evenements'),
    path('evenements/ajouter/', views.ajouter_evenement, name='ajouter_evenement'),
    path('evenements/modifier/<int:evenement_id>/', views.modifier_evenement, name='modifier_evenement'),
    path('evenements/supprimer/<int:evenement_id>/', views.supprimer_evenement, name='supprimer_evenement'),

    # Gestion des réservations d'événements
    path('reservations/', views.liste_reservations, name='liste_reservations'),
    path('reservations/ajouter/<int:evenement_id>/', views.ajouter_reservation, name='ajouter_reservation'),
    path('reservations/supprimer/<int:reservation_id>/', views.supprimer_reservation, name='supprimer_reservation'),
    path('reservations/modifier/<int:reservation_id>/', views.modifier_reservation, name='modifier_reservation'),

    # Gestion des chambres
    path('chambres/', views.liste_chambres, name='liste_chambres'),
    path('chambres/ajouter/', views.ajouter_chambre, name='ajouter_chambre'),
    path('chambres/modifier/<int:chambre_id>/', views.modifier_chambre, name='modifier_chambre'),
    path('chambres/supprimer/<int:chambre_id>/', views.supprimer_chambre, name='supprimer_chambre'),

    # Gestion des réservations de chambres
    path('reservations-chambres/', views.liste_reservations_chambres, name='liste_reservations_chambres'),
    path('reservations-chambres/ajouter/', views.ajouter_reservation_chambre, name='ajouter_reservation_chambre'),
    path('reservations-chambres/modifier/<int:reservation_id>/', views.modifier_reservation_chambre, name='modifier_reservation_chambre'),
    path('reservations-chambres/supprimer/<int:reservation_id>/', views.supprimer_reservation_chambre, name='supprimer_reservation_chambre'),

    # Gestion des plats journaliers
    # path('plats-journaliers/', liste_plats_journaliers, name='liste_plats_journaliers'),
    # path('plats-journaliers/ajouter/<int:reservation_id>/', ajouter_plat_journalier, name='ajouter_plat_journalier'),
    # path('plats-journaliers/supprimer/<int:plat_journalier_id>/', supprimer_plat_journalier, name='supprimer_plat_journalier'),
]