from django.db import models
from suppliers.models import Fournisseur

STATUT_CHOICES = [
    ('En attente de traitement', 'En Attente De Traitement'),
    ('En cours de traitement', 'En Cours De Traitement'),
    ('Livré à temps', 'Livré A Temps'),
    ('Livré en retard', 'Livré En Retard')
]

class Commande(models.Model):

    nom = models.CharField(max_length=45, null=True, unique=True)
    date_commande = models.DateField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES, default='En Attente De Traitement')

    def __str__(self) -> str:
        return self.nom
    
