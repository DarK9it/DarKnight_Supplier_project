from django.forms import ModelForm
from suppliers.models import Paiement

class PaiementForm(ModelForm):
    class Meta:
        model = Paiement
        fields = '__all__'