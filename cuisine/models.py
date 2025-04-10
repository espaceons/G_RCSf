from django.db import models

from stock.models import Ingredient


class Plat(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through='Recette')

    def __str__(self):
        return self.nom

    def reduire_stock(self, quantite_preparation=1):
        """
        Réduit les ingrédients du stock en fonction de la quantité préparée.
        """
        for recette in self.recette_set.all():
            ingredient = recette.ingredient
            quantite_necessaire = recette.quantite_necessaire * quantite_preparation

            # Vérifie si le stock est suffisant
            if ingredient.quantite_stock >= quantite_necessaire:
                ingredient.quantite_stock -= quantite_necessaire
                ingredient.save()
            else:
                raise ValueError(f"Stock insuffisant pour l'ingrédient {ingredient.nom}")

class Recette(models.Model):
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite_necessaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.plat.nom} - {self.ingredient.nom}"