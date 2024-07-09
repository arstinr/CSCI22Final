from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'webkiosk'
urlpatterns = [
    path('', views.index),
    path('customers/', views.listcustomers, name='customer-list'),
    path('customer/new/', views.addcustomer, name='customer-add'),
    path('customer/<int:pk>/', views.listcustomerdetails, name='customer-details'),
    path('customer/<int:pk>/edit/', views.editcustomerdetails, name="customer-edit"),
    path('customer/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),
    path('customer/<int:customer_id>/address/new/', views.addaddress, name='address-add'),

    path('food/new/', views.addfood, name='food-add'),
    path('food/<int:pk>/', views.listfooddetails, name='food-details'),
    path('food/<int:pk>/edit/', views.editfooddetails, name='food-edit'),
    path('food/<int:pk>/delete/', views.deletefood, name="food-delete"),
    path('foods/', views.listfood, name='food-list'),

    path('customer/<int:customer_id>/order/new/', views.addordertocustomer, name='order-add-customer'),
    path('order/new/', views.addorder, name='order-add'),
    path('order/<int:pk>/', views.listorderdetails, name='order-details'),
    path('order/<int:pk>/edit/', views.editorderdetails, name='order-edit'),
    path('order/<int:pk>/delete/', views.deleteorder, name="order-delete"),
    path('order/<int:pk>/items/add/', views.addorderitem, name='orderitem-add'),
]