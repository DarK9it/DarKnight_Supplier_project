from django.forms import ModelForm
from suppliers.models import NoteFournisseur

class NoteFournisseurForm(ModelForm):
    class Meta:
        model = NoteFournisseur
        fields = '__all__'