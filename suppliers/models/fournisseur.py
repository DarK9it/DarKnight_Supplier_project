from django.db import models

class Fournisseur(models.Model):
    
    nom_entreprise = models.CharField(max_length=45, null=True)
    adresse = models.CharField(max_length=45, null=True)
    telephone= models.CharField(max_length=45, null=True)
    
    def __str__(self) -> str:
        return self.nom
