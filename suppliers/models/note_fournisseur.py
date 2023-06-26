from django.db import models
from suppliers.models import Fournisseur

class NoteFournisseur(models.Model):
    
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    note = models.FloatField()
    commentaire = models.CharField(max_length=45, null=True)
 