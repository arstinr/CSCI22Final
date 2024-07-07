from django.forms import ModelForm, HiddenInput
from .models import Customer, Address, Food

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']

class AddAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = {'street', 'city', 'customer'}
        widgets = { 'customer': HiddenInput()}

class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = {'name','description','price'}
