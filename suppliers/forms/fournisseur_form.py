from django.forms import ModelForm
from suppliers.models import Fournisseur

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'