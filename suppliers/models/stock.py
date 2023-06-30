from django.db import models
from suppliers.models import Produit, CategorieProduit

class Stock(models.Model):
    
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.FloatField()
    categorie = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.quantite < 1:
            self.produit.statut = 'Rupture de stock'
        else:
            self.produit.statut = 'Disponible'
        self.produit.save()