from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'webkiosk'
urlpatterns = [
    path('', views.index),
    path('customers/', views.listcustomers, name='customer-list'),
    path('customer/new/', views.addcustomer, name='add-customer'),
    path('customer/<int:pk>/', views.listcustomerdetails, name='customer-details')
]