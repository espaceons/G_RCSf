from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm

from django.contrib.auth import authenticate, login

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('accueil')  # Redirige vers la page d'accueil ou une autre page
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
            return redirect('accueil')  # Redirige vers la page d'accueil ou une autre page
        else:
            return render(request, 'authentification/connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'authentification/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')  # Redirige vers la page de connexion