from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    TYPE_UTILISATEUR_CHOICES = [
        ('STAGIAIRE', 'Stagiaire'),
        ('APPRENTI', 'Apprenti'),
        ('ETUDIANT', 'Étudiant'),
        ('PASSAGER', 'Passager'),
    ]

    # Type d'utilisateur (stagiaire, apprenti, etc.)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_UTILISATEUR_CHOICES, blank=True, null=True)

    def __str__(self):
        """
        Méthode pour afficher un utilisateur de manière lisible.
        Exemple : "John Doe (Stagiaire)"
        """
        return f"{self.username} ({self.get_type_utilisateur_display()})"