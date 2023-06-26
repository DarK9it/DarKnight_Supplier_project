from django.db import models
from suppliers.models import Produit

class HistoriquePrix(models.Model):
    
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_prix = models.DateField()
    prix = models.FloatField()
 