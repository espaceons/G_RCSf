from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    quantite_stock = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=20)  # Ex: kg, L, unité

    def __str__(self):
        return f"{self.nom} ({self.quantite_stock} {self.unite})"
    
    
class Achat(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Achat de {self.ingredient.nom} chez {self.fournisseur.nom}"