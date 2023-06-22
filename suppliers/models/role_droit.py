from django.db import models

from activites.models import Droit
from activites.models import Role

class RoleDroit(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    droit = models.ForeignKey(Droit, on_delete=models.CASCADE)
    