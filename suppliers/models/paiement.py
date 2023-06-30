from django.db import models
from suppliers.models import Commande, Facture

STATUT_CHOICES = [
    ('Non traité', 'Non Traité')
]

class Paiement(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=False)
    montant = models.FloatField()
    date_paiement = models.DateField()
    mode_paiement = models.CharField(max_length=200, null=True)
    numero_virement = models.CharField(max_length=200, null=True)
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES, default='Non Traité')

    def save(self, *args, **kwargs):
        if self.facture.statut == 'validé':
            self.statut = 'Traité'
        else:
            self.statut = 'Non Traité'
        super(Paiement, self).save(*args, **kwargs)