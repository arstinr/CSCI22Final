from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Customer, Address, Food
from .forms import AddCustomerForm, AddAddressForm, AddFoodForm

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
def addfood(request):
    if request.method == 'GET':
        aff = AddFoodForm()
    elif request.method == 'POST':
        aff = AddFoodForm(request.POST)
        if aff.is_valid():
            aff.save()
            return redirect('webkiosk:food-list')
    
    context = {'form': aff}
    return render(request, 'webkiosk/food_form.html', context)

#View for viewing complete details of a food record/ def listfooddetails
def listfooddetails(request, pk):
    f = get_object_or_404(Food, id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

#View for editing details of food record/ def editfooddetails
#View for deleting a food record/ def deletefood

##View All Food Records
#Create page that lists all food records in db / listfood
#For attributes, only show name and price
#Each item in list should have links: 
#   Show more info about record, edit, delete

#-------------------------------------------------------------------------#

##ORDER
#View for adding new Order
#View for viewing complete details of an order record
#   should include: list of all items and total price of each (qty * price)
#   total price of entire order should be shown

#View for editing details of an order
#View for deleting order

##ORDERITEM
# must be integrated with adding of Order record (extends order?)
# contains: drop-down to select user the order is for
# must be able to add multiple order items to a single order & specify qty for each item
# user must be able to delete existing items from an order
# when viewing details of order, should list all order items from an order

##View all orders
#Create page that lists all order records in db
# for attributes show only: order id, customer full name, date n time of order
# each item in list should have links: more info abt record, edit, delete

##Modify customer details to include:
#   - list of all orders customer has made(order id, date n time)
#       - should have link to view order details
#   - each customer details page should have "Add Order" button
#       - leads to add order form where selected customer is automatically set as customer for that order

