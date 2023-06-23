from django.forms import ModelForm
from suppliers.models import CategorieProduit

class CategorieProduitForm(ModelForm):
    class Meta:
        model = CategorieProduit
        fields = '__all__'