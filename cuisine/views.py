from django.shortcuts import get_object_or_404, redirect, render

from cuisine.forms import PlatForm
from .models import Plat

# Vue pour lister les plats
def liste_plats(request):
    plats = Plat.objects.all()
    return render(request, 'cuisine/liste_plats.html', {'plats': plats})


# Vue pour ajouter un plat
def ajouter_plat(request):
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_plats')
    else:
        form = PlatForm()
    return render(request, 'cuisine/ajouter_plat.html', {'form': form})


# Vue pour modifier un plat
def modifier_plat(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)
    if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('liste_plats')
    else:
        form = PlatForm(instance=plat)
    return render(request, 'cuisine/modifier_plat.html', {'form': form, 'plat': plat})


# Vue pour supprimer un plat
def supprimer_plat(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)
    if request.method == 'POST':
        plat.delete()
        return redirect('liste_plats')
    return render(request, 'cuisine/supprimer_plat.html', {'plat': plat})