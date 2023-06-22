from django.db import models
from suppliers.models import Fournisseur, CategorieProduit

class Produit(models.Model):
    
    nom = models.CharField()
    desscription = models.CharField()
    prix = models.FloatField()
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)
    