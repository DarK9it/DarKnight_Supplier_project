from django.db import models
from suppliers.models import Commande, Fournisseur

class Facture(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True, default=None)
    date_facture = models.DateField()
    montant_total = models.FloatField()
    numero_facture = models.IntegerField(default=0)
    