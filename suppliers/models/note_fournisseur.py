from django.db import models
from suppliers.models import Fournisseur

class NoteFournisseur(models.Model):
    
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    note = models.FloatField()
    commentaire = models.CharField()
 