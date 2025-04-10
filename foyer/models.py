from django.db import models
from django.forms import ValidationError
from authentification.models import Utilisateur  # Importez le modèle Utilisateur depuis authentification

class Evenement(models.Model):
    # Titre de l'événement (ex: "Soirée Cinéma", "Conférence")
    titre = models.CharField(max_length=100)

    # Date de début de l'événement
    date_debut = models.DateField()

    # Date de fin de l'événement
    date_fin = models.DateField()

    # Description détaillée de l'événement
    description = models.TextField()
    
    def clean(self):
        if self.date_debut and self.date_fin and self.date_debut > self.date_fin:
            raise ValidationError("La date de début doit être antérieure ou égale à la date de fin.")

    def __str__(self):
        """
        Méthode pour afficher un objet Evenement de manière lisible.
        Exemple : "Soirée Cinéma (du 2023-10-01 au 2023-10-05)"
        """
        return f"{self.titre} (du {self.date_debut} au {self.date_fin})"


# Modèle pour gérer les réservations aux événements
class Reservation(models.Model):
    # Relation avec le modèle Evenement (chaque réservation est liée à un événement)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)

    # Relation avec l'utilisateur authentifié
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    # Numéro de téléphone du client
    telephone = models.CharField(max_length=20)

    # Date et heure automatique de la réservation (ajoutée lors de la création)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Méthode pour afficher une réservation de manière lisible.
        Exemple : "Réservation pour evennement de soirée"
        """
        return f"Réservation pour {self.evenement.titre} par {self.utilisateur}"


# Modèle pour gérer les chambres disponibles dans le foyer
class Chambre(models.Model):
    # Choix possibles pour le statut d'une chambre
    STATUT_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('INDISPONIBLE', 'Indisponible'),
        ('MAINTENANCE', 'En maintenance'),
    ]

    # Numéro unique de la chambre (ex: "101", "202")
    numero = models.CharField(max_length=10, unique=True)

    # Capacité de la chambre (nombre de personnes pouvant être hébergées)
    capacite = models.IntegerField()

    # Statut de la chambre (disponible, indisponible, en maintenance)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='DISPONIBLE')

    def __str__(self):
        """
        Méthode pour afficher une chambre de manière lisible.
        Exemple : "Chambre 101 (2 personnes) - Disponible"
        """
        return f"Chambre {self.numero} ({self.capacite} personnes) - {self.get_statut_display()}"


# Modèle pour gérer les options de pension (demi-pension ou pension complète)
class Pension(models.Model):
    # Choix possibles pour le type de pension
    TYPE_PENSION_CHOICES = [
        ('DEMI', 'Demi-pension'),  # Demi-pension : repas du soir inclus
        ('COMPLETE', 'Pension complète')  # Pension complète : petits-déjeuners, déjeuners et dîners inclus
    ]

    # Type de pension sélectionné (parmi les choix définis ci-dessus)
    type_pension = models.CharField(max_length=10, choices=TYPE_PENSION_CHOICES)

    # Prix associé à l'option de pension
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Méthode pour afficher une option de pension de manière lisible.
        Exemple : "Demi-pension - 50.00€"
        """
        return f"{self.get_type_pension_display()} - {self.prix}€"


# Modèle pour gérer les réservations de chambres avec une option de pension
class ReservationChambre(models.Model):
    # Relation avec le modèle Chambre (chaque réservation est liée à une chambre)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)

    # Relation avec le modèle Pension (chaque réservation inclut une option de pension)
    pension = models.ForeignKey(Pension, on_delete=models.CASCADE)

    # Date de début de la réservation
    date_debut = models.DateField()

    # Date de fin de la réservation
    date_fin = models.DateField()

    # Relation avec l'utilisateur authentifié
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        """
        Méthode pour afficher une réservation de chambre de manière lisible.
        Exemple : "Réservation de John Doe pour Chambre 101"
        """
        return f"Réservation de {self.nom_client} pour {self.chambre.numero}"


# Modèle pour attribuer un plat journalier à une réservation de chambre
class PlatJournalier(models.Model):
    # Relation avec le modèle ReservationChambre (chaque plat est lié à une réservation de chambre)
    reservation = models.ForeignKey(ReservationChambre, on_delete=models.CASCADE)

    # Relation avec le modèle Plat (chaque plat est lié à un plat défini dans l'application cuisine)
    plat = models.ForeignKey('cuisine.Plat', on_delete=models.CASCADE)

    # Date à laquelle le plat est attribué
    date = models.DateField()

    def __str__(self):
        """
        Méthode pour afficher un plat journalier de manière lisible.
        Exemple : "Pizza Margherita pour John Doe le 2023-10-15"
        """
        return f"{self.plat.nom} pour {self.reservation.nom_client} le {self.date}"