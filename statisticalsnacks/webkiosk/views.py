from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Address
from .forms import AddCustomerForm

# Create your views here.

def index(request):
    return render(request, "webkiosk/base_template.html")

def listcustomers(request):
    customerlist = Customer.objects.all()
    context = {'customerlist': customerlist}
    return render(request, "webkiosk/customer_list.html", context)

def addcustomer(request):
    if request.method == 'GET':
        acf = AddCustomerForm()
    elif request.method == 'POST':
        acf = AddCustomerForm(request.POST)
        if acf.is_valid():
            acf.save()
    
    context = {'form': acf}
    return render(request, 'webkiosk/customer_form.html', context)
