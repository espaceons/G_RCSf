from django.urls import path
from . import views


app_name = 'restaurant'

urlpatterns = [
    path('tables/', views.liste_tables, name='liste_tables'),
]