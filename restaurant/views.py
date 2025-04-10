from django.shortcuts import render
from .models import Table

def liste_tables(request):
    tables = Table.objects.all()  # Récupérer toutes les tables
    return render(request, 'restaurant/liste_tables.html', {'tables': tables})