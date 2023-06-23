from django.forms import ModelForm
from suppliers.models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'