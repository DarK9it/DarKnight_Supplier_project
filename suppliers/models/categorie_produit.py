from django.db import models

class CategorieProduit(models.Model):
    
    nom_categorie = models.CharField(max_length=45, null=False)
    
    def __str__(self) -> str:
        return self.nom_categorie