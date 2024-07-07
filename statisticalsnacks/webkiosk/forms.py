from django.forms import ModelForm, HiddenInput
from .models import Customer, Address

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']

class AddAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = {'street', 'city', 'customer'}
        widgets = { 'customer': HiddenInput()}
