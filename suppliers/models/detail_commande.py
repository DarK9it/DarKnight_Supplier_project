from django.db import models
from suppliers.models import Commande, Produit

class DetailCommande(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.FloatField()
    prix_total = models.FloatField()