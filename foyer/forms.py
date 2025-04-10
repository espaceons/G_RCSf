from django import forms
from .models import Evenement, Reservation, Chambre, ReservationChambre, PlatJournalier

# Formulaire pour les événements
class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['titre', 'date_debut', 'date_fin', 'description']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin and date_debut > date_fin:
            raise forms.ValidationError("La date de début doit être antérieure ou égale à la date de fin.")

# Formulaire pour les réservations d'événements
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['evenement', 'utilisateur', 'telephone']

# Formulaire pour les chambres
class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'capacite', 'statut']
        widgets = {
            'statut': forms.Select(choices=Chambre.STATUT_CHOICES),
        }

# Formulaire pour les réservations de chambres
class ReservationChambreForm(forms.ModelForm):
    class Meta:
        model = ReservationChambre
        fields = ['chambre', 'pension', 'date_debut', 'date_fin', 'utilisateur']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulaire pour les plats journaliers
#class PlatJournalierForm(forms.ModelForm):
#    class Meta:
#        model = PlatJournalier
#        fields = ['reservation', 'plat', 'date']
#        widgets = {
#            'date': forms.DateInput(attrs={'type': 'date'}),
#        }