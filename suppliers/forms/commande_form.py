from django.forms import ModelForm
from suppliers.models import Commande

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'