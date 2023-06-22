from django.db import models

class Droit(models.Model):
    nom = models.CharField(max_length=45, null=True)
    
    def __str__(self) -> str:
        return self.nom
    