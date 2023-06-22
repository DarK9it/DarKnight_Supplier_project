from django.db import models
from suppliers.models import Role
from django.contrib.auth.models import User

class UserRole(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    