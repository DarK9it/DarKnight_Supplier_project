from django.db import models
from suppliers.models import Commande

class Facture(models.Model):
    
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_facture = models.DateField()
    montant_total = models.FloatField()