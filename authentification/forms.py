from django import forms
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    type_utilisateur = forms.ChoiceField(
        choices=Utilisateur.TYPE_UTILISATEUR_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    class Meta:
        model = Utilisateur
        fields = ['username', 'email','telephone', 'type_utilisateur']