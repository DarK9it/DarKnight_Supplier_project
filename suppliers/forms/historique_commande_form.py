from django.forms import ModelForm
from suppliers.models import HistoriqueCommande

class HistoriqueCommandeForm(ModelForm):
    class Meta:
        model = HistoriqueCommande
        fields = '__all__'