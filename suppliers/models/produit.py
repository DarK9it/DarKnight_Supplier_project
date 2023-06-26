from django.db import models
from suppliers.models import Fournisseur, CategorieProduit

class Produit(models.Model):
    
    nom = models.CharField(max_length=45, null=True)
    desscription = models.CharField(max_length=45, null=True)
    prix = models.FloatField()
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom
    