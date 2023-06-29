from django.db import models
from suppliers.models import Commande

class HistoriqueCommande(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_modification = models.DateField()
    commentaire = models.CharField(max_length=200, null=True)