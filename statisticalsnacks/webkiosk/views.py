from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
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
            return redirect('webkiosk:customer-list')
    
    context = {'form': acf, 'actionname': 'Add Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def listcustomerdetails(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def editcustomerdetails(request, pk):
    customer = Customer.objects.get(id=pk)
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
    c = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = { 'customer': c}
        return render(request, 'webkiosk/customer_delete.html',context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')
