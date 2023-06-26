from django.db import models
from suppliers.models import Fournisseur

class Commande(models.Model):
    
    nom = models.CharField(max_length=45, null=True)
    date_commande = models.DateField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.id
