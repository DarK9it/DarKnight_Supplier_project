from django.db import models
from suppliers.models import Commande, Facture

STATUT_CHOICES = [
    ('Non traité', 'Non Traité'),
    ('Traité', 'Traité')
]

class Paiement(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=True, default=None)
    montant = models.FloatField()
    date_paiement = models.DateField()
    mode_paiement = models.CharField(max_length=200, null=True)
    numero_virement = models.CharField(max_length=200, null=True, unique=True)
    status = models.CharField(max_length=100, choices=STATUT_CHOICES, default='Non traité')
