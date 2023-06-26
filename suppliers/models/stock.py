from django.db import models
from suppliers.models import Produit

class Stock(models.Model):
    
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.FloatField()