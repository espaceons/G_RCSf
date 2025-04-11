
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evenement
from foyer.forms import EvenementForm
from datetime import date
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationChambreForm, ReservationForm

#Application Evenement :
#-------------------------

# Liste des événements
def liste_evenements(request):
    evenements = Evenement.objects.all()
    return render(request, 'foyer/liste_evenements.html', {'evenements': evenements})

# Ajouter un événement
def ajouter_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foyer:liste_evenements')
    else:
        form = EvenementForm()
    return render(request, 'foyer/ajouter_evenement.html', {'form': form})

# Modifier un événement
def modifier_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    if request.method == 'POST':
        form = EvenementForm(request.POST, instance=evenement)
        if form.is_valid():
            form.save()
            return redirect('foyer:liste_evenements')
    else:
        form = EvenementForm(instance=evenement)
    return render(request, 'foyer/modifier_evenement.html', {'form': form})

# Supprimer un événement
def supprimer_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    if request.method == 'POST':
        evenement.delete()
        return redirect('foyer:liste_evenements')
    return render(request, 'foyer/supprimer_evenement.html', {'evenement': evenement})




# application réservation evenement:
#-------------------------

# Liste des réservations evenement





@login_required
def liste_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'foyer/liste_reservations.html', {'reservations': reservations})

# Vue pour ajouter une réservation pour un événement spécifique

@login_required
def ajouter_reservation(request):
    # Filtrer les événements dont la date de début est future ou égale à aujourd'hui
    evenements_futurs = Evenement.objects.filter(date_debut__gte=date.today())

    if request.method == 'POST':
        telephone = request.POST.get('telephone') # Récupération du numéro de téléphone
        evenement_ids = request.POST.getlist('evenements') #Recuperation des IDs des evenement
        
        if not request.user.is_authenticated: #Verification de l'authentification.
            messages.error(request, "Vous devez être connecté pour faire une réservation.")
            return redirect('login') #Redirection vers la page login

        for evenement_id in evenement_ids:
            evenement = Evenement.objects.get(id=evenement_id)
            
            # Vérifier si une réservation existe déjà
            if Reservation.objects.filter(utilisateur=request.user, evenement=evenement).exists():
                messages.error(request, f"Vous avez déjà une réservation pour l'événement '{evenement.titre}'.")
                continue  # Passer à l'événement suivant
            Reservation.objects.create(
                evenement=evenement,
                utilisateur=request.user #Recuperation de l'utilisateur
            )
        return redirect('foyer:liste_reservations')
    context = {
        'evenements_futurs': evenements_futurs,
        'form' : ReservationForm()
    }
    return render(request, 'foyer/ajouter_reservation.html', context)

# Vue pour supprimer une réservation evenement:

@login_required
def supprimer_reservation(request, reservation_id):
    # Récupérer la réservation correspondante à l'ID fourni
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.method == 'POST':
        # Si la méthode est POST, supprimer la réservation
        reservation.delete()
        return redirect('foyer:liste_reservations')  # Rediriger vers la liste des réservations
    
    # Afficher un message de confirmation avant la suppression
    return render(request, 'foyer/supprimer_reservation.html', {'reservation': reservation})

# Vue pour modifier une réservation evenement

@login_required
def modifier_reservation(request, reservation_id):
    # Récupérer la réservation correspondante à l'ID fourni
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.method == 'POST':
        # Si le formulaire est soumis, valider les données
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('liste_reservations')  # Rediriger vers la liste des réservations
    else:
        # Pré-remplir le formulaire avec les données actuelles de la réservation
        form = ReservationForm(instance=reservation)
    
    # Rendre le template avec le formulaire
    return render(request, 'foyer/modifier_reservation.html', {'form': form, 'reservation': reservation})

# application réservation chambre :
#---------------------------------

@login_required
def liste_reservations_chambres(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.evenement = evenement
            reservation.utilisateur = request.user
            reservation.save()
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'foyer/ajouter_reservation.html', {'form': form, 'evenement': evenement})


# Vue pour ajouter une réservation de chambre
def ajouter_reservation_chambre(request):
    if request.method == 'POST':
        # Si le formulaire est soumis, le valider et sauvegarder les données
        form = ReservationChambreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_reservations_chambres')  # Rediriger vers la liste des réservations de chambres
    else:
        # Afficher un formulaire vide
        form = ReservationChambreForm()
    
    # Rendre le template avec le formulaire
    return render(request, 'foyer/ajouter_reservation_chambre.html', {'form': form})


# Vue pour modifier une réservation
def modifier_reservation_chambre(request, reservation_id):
    # Récupérer la réservation à modifier
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.method == 'POST':
        # Si le formulaire est soumis, le valider et sauvegarder les modifications
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('liste_reservations')  # Rediriger vers la liste des réservations
    else:
        # Pré-remplir le formulaire avec les données actuelles de la réservation
        form = ReservationForm(instance=reservation)
    
    # Rendre le template avec le formulaire
    return render(request, 'foyer/modifier_reservation.html', {'form': form, 'reservation': reservation})

# Supprimer une réservation
@login_required
def supprimer_reservation_chambre(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, utilisateur=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('liste_reservations')
    return render(request, 'foyer/supprimer_reservation.html', {'reservation': reservation})


# application chambre:
#---------------------


from .models import Chambre
from .forms import ChambreForm

# Liste des chambres
def liste_chambres(request):
    chambres = Chambre.objects.all()
    return render(request, 'foyer/liste_chambres.html', {'chambres': chambres})

# Ajouter une chambre
def ajouter_chambre(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foyer:liste_chambres')
    else:
        form = ChambreForm()
    return render(request, 'foyer/ajouter_chambre.html', {'form': form})

# Modifier une chambre
def modifier_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambre, id=chambre_id)
    if request.method == 'POST':
        form = ChambreForm(request.POST, instance=chambre)
        if form.is_valid():
            form.save()
            return redirect('foyer:liste_chambres')
    else:
        form = ChambreForm(instance=chambre)
    return render(request, 'foyer/modifier_chambre.html', {'form': form})

# Supprimer une chambre
def supprimer_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambre, id=chambre_id)
    if request.method == 'POST':
        chambre.delete()
        return redirect('foyer:liste_chambres')
    return render(request, 'foyer/supprimer_chambre.html', {'chambre': chambre})



# Vue pour le sous-dashboard de Foyer
def sous_dashboard_foyer(request):
    context = {
        'menu': [
            {'name': 'Chambres', 'url': 'foyer:liste_chambres', 'description': 'Gérer les chambres.'},
            {'name': 'Réservations', 'url': 'foyer:liste_reservations', 'description': 'Gérer les réservations.'},
            {'name': 'Événements', 'url': 'foyer:liste_evenements', 'description': 'Gérer les événements.'},
        ]
    }
    return render(request, 'foyer/sous_dashboard_foyer.html', context)
