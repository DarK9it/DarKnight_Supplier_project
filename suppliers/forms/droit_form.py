from django.forms import ModelForm
from suppliers.models import Droit

class DroitForm(ModelForm):
    class Meta:
        model = Droit
        fields = '__all__'