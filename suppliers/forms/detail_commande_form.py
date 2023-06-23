from django.forms import ModelForm
from suppliers.models import DetailCommande

class DetailCommandeForm(ModelForm):
    class Meta:
        model = DetailCommande
        fields = '__all__'