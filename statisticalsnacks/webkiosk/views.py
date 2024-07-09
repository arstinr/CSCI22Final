from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Customer, Address, Food, Order, OrderItem
from .forms import AddCustomerForm, AddAddressForm, AddFoodForm, AddOrderForm, AddOrderItemForm

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
#widgets = { 'customer': HiddenInput()}
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
    
    context = {'form': aff, 'actionname': 'Add Food'}
    return render(request, 'webkiosk/food_form.html', context)

#View for viewing complete details of a food record/ def listfooddetails
def listfooddetails(request, pk):
    f = get_object_or_404(Food, id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

#View for editing details of food record/ def editfooddetails
def editfooddetails(request, pk):
    food = get_object_or_404(Food, id=pk)
    if request.method == 'GET':
        form = AddFoodForm(instance=food)
    elif request.method == 'POST':
        form = AddFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request,'Food record updated succesfully!')
            return redirect('webkiosk:food-details',pk)

    context = {'form':form,  'actionname': 'Edit Food'}
    return render(request, 'webkiosk/food_form.html', context)

#View for deleting a food record/ def deletefood
def deletefood(request, pk):
    f = get_object_or_404(Food, id=pk)
    if request.method == 'GET':
        context = { 'food': f}
        return render(request, 'webkiosk/food_delete.html',context)
    elif request.method == 'POST':
        f.delete()
        return redirect('webkiosk:food-list')

##View All Food Records
#Create page that lists all food records in db / listfood
#For attributes, only show name and price
#Each item in list should have links: 
#   Show more info about record, edit, delete
def listfood(request):
    foodlist = Food.objects.all()
    context = {'foodlist': foodlist}
    return render(request, "webkiosk/food_list.html", context)

#-------------------------------------------------------------------------#

##ORDER
#View for adding new Order
def addorder(request):
    if request.method == 'GET':
        aof = AddOrderForm()
    elif request.method == 'POST':
        aof = AddOrderForm(request.POST)
        if aof.is_valid():
            order = aof.save()
            return redirect('webkiosk:orderitem-add', pk=order.id)
    
    context = {'form': aof, 'actionname': 'Add Order'}
    return render(request, 'webkiosk/order_form.html', context)

##FOR CUSTOMERVIEW TO ADD ORDER
def addordertocustomer(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, id=customer_id)
        form = AddOrderForm(initial={'customer': customer})
    elif request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('webkiosk:orderitem-add', pk=order.id)
    
    context = {'form':form, 'actionname': 'Add Order to Customer'}
    return render(request, 'webkiosk/order_form.html', context)

#View for viewing complete details of an order record
#   should include: list of all items and total price of each (qty * price)
#   total price of entire order should be shown
def listorderdetails(request, pk):
    o = get_object_or_404(Order, id=pk)
    context = {'order': o}
    return render(request, 'webkiosk/order_detail.html', context)

#View for editing details of an order
def editorderdetails(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'GET':
        form = AddOrderForm(instance=order)
    elif request.method == 'POST':
        form = AddOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'Order record updated succesfully!')
            return redirect('webkiosk:order-details',pk)

    context = {'form':form,  'actionname': 'Edit Order'}
    return render(request, 'webkiosk/order_form.html', context)

#View for deleting order
def deleteorder(request, pk):
    o = get_object_or_404(Order, id=pk)
    if request.method == 'GET':
        context = { 'order': o}
        return render(request, 'webkiosk/order_delete.html',context)
    elif request.method == 'POST':
        o.delete()
        return redirect('webkiosk:order-list')


##ORDERITEM
# must be integrated with adding of Order record (extends order?)
# contains: drop-down to select user the order is for
# must be able to add multiple order items to a single order & specify qty for each item
# user must be able to delete existing items from an order
# when viewing details of order, should list all order items from an order
def addorderitem(request, pk):
    if request.method == 'GET':
        order = get_object_or_404(Order, id=pk)
        form = AddOrderItemForm(initial={'order': order})
    elif request.method == 'POST':
        form = AddOrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:orderitem-add',pk)
            #redirect to order saved page(?) with back button
    
    context = {'form':form, 'actionname': 'Add Order Items'}
    return render(request, 'webkiosk/orderitem_form.html', context)


##View all orders
#Create page that lists all order records in db
# for attributes show only: order id, customer full name, date n time of order
# each item in list should have links: more info abt record, edit, delete

def listorders(request):
    orderlist = Order.objects.all()
    context = {'orderlist': orderlist}
    return render(request, "webkiosk/order_list.html", context)

##Modify customer details to include:
#   - list of all orders customer has made(order id, date n time)
#       - should have link to view order details
#   - each customer details page should have "Add Order" button
#       - leads to add order form where selected customer is automatically set as customer for that order

