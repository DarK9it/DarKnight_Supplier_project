from django.db import models
from suppliers.models import Fournisseur

class Commande(models.Model):
    
    date_commande = models.DateField()
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    