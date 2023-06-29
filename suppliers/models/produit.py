from django.db import models
from suppliers.models import Fournisseur, CategorieProduit

class Produit(models.Model):
    
    nom = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=200, null=True)
    prix = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)
    delais = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.nom + " " + self.description
    