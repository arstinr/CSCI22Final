from django.forms import ModelForm
from .models import Customer

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']
