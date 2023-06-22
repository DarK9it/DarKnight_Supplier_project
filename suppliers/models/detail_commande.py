from django.db import models
from suppliers.models import Commande, Produit

class DetailCommande(models.Model):
    
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.FloatField()