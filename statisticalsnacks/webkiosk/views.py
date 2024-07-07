from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Customer, Address
from .forms import AddCustomerForm, AddAddressForm

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
            return redirect('webkiosk:customer-list')
    
    context = {'form': acf, 'actionname': 'Add Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def listcustomerdetails(request, pk):
    c = get_object_or_404(Customer, id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def editcustomerdetails(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'GET':
        form = AddCustomerForm(instance=customer)
    elif request.method == 'POST':
        form = AddCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer record updated succesfully!')
    context = {'form':form,  'actionname': 'Edit Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    c = get_object_or_404(Customer, id=pk)
    if request.method == 'GET':
        context = { 'customer': c}
        return render(request, 'webkiosk/customer_delete.html',context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')
    
def addaddress(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, id=customer_id)
        form = AddAddressForm(initial={'customer': customer})
    elif request.method == 'POST':
        form = AddAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:customer-details',pk=customer_id)
    
    context = {'form':form}
    return render(request, 'webkiosk/address_form.html', context)

##Food
#View for adding new food records
#View for viewing complete details of a food record
#View for editing details of food record
#View for deleting a food record

##View All Food Records
#Create page that lists all food records in db
#For attributes, only show name and price
#Each item in list should have links: 
#   Show more info about record, edit, delete