from django.forms import ModelForm
from suppliers.models import RoleDroit

class RoleDroitForm(ModelForm):
    class Meta:
        model = RoleDroit
        fields = '__all__'