from django.db import models

class Table(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    capacite = models.IntegerField()

    def __str__(self):
        return f"Table {self.numero} ({self.capacite} personnes)"

class Commande(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Commande de la table {self.table.numero}"