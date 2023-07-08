from django.db import models
from suppliers.models import Commande, Produit, CategorieProduit

class DetailCommande(models.Model):
    
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.FloatField()
    prix_total = models.FloatField()