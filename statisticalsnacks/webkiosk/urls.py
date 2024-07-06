from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('customers/', views.listcustomers, name='customer-list'),
    path('customer/new/', views.addcustomer, name='add-customer'),
]