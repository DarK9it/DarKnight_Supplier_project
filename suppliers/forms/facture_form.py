from django.forms import ModelForm
from suppliers.models import Facture

class FactureForm(ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'