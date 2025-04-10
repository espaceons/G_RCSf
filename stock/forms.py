from django import forms
from .models import Ingredient
from .models import Fournisseur


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nom', 'quantite_stock', 'unite']
        
        
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'telephone']