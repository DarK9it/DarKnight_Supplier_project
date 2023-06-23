from django.forms import ModelForm
from suppliers.models import Role

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'