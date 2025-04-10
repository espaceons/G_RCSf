from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('login/', views.connexion, name='login'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
]