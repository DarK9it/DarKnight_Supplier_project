from django.db import models
from suppliers.models import Commande

class Paiement(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant = models.FloatField()
    date_paiement = models.DateField()
    