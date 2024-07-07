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
    path('food/<int:pk>/', views.listfooddetails, name='food-details')
    
]