from django.db import models

from suppliers.models import Droit
from suppliers.models import Role

class RoleDroit(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    droit = models.ForeignKey(Droit, on_delete=models.CASCADE)
    