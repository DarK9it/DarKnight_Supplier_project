from django.db import models

class Role(models.Model):
    
    nom = models.CharField(max_length=45, null=True, unique=True)
    
    def __str__(self) -> str:
        return self.nom
    