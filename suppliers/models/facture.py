from django.db import models
from suppliers.models import Commande, Fournisseur

STATUT_CHOICES = [
    ('validé', 'Validé'),
    ('Non validé', 'Non Validé')
]

class Facture(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True, default=None)
    date_facture = models.DateField()
    montant_total = models.FloatField()
    numero_facture = models.CharField(max_length=45, null=True, unique=True)
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES, default='Non validé')

    def __str__(self)-> str:
        return self.numero_facture