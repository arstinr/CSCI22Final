from django import forms
from django.forms import ModelForm, HiddenInput, Select
from .models import Customer, Address, Food, Order, OrderItem

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']

class AddAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'customer']
        widgets = { 'customer': HiddenInput()}

class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name','description','price']

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['paymentmode', 'customer']

class AddOrderItemForm(ModelForm):
    food = forms.ModelChoiceField(
        queryset=Food.objects.all(),
        empty_label="Select Item"
        label="Food Item"
        #widget= forms.Select(attrs={'class': 'selectFoodItem'})
    )
    class Meta:
        model = OrderItem
        fields = ['quantity', 'food']
        widgets = {'customer':HiddenInput()}
        