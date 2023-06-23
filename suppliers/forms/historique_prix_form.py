from django.forms import ModelForm
from suppliers.models import HistoriquePrix

class HistoriquePrixForm(ModelForm):
    class Meta:
        model = HistoriquePrix
        fields = '__all__'