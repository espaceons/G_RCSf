from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.type_utilisateur = form.cleaned_data['type_utilisateur'] # recuperer le type d'utilisateur
            user.telephone = form.cleaned_data['telephone'] # recuperer le telephone
                        
            user.save()
            login(request, user)
            messages.success(request, 'Inscription réussie !')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erreur lors de l\'inscription. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = InscriptionForm()
    return render(request, 'authentification/inscription.html', {'form': form})





def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige vers la page d'accueil ou une autre page
        else:
            return render(request, 'authentification/connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'authentification/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('comptes:login')  # Redirige vers la page de connexion