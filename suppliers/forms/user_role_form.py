from django.forms import ModelForm
from suppliers.models import UserRole

class UserRoleForm(ModelForm):
    class Meta:
        model = UserRole
        fields = '__all__'