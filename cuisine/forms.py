from django import forms
from .models import Plat

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['nom', 'description', 'prix', 'ingredients']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }