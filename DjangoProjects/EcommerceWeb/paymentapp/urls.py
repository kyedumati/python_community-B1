from django.contrib import admin
from django.urls import path
from paymentapp import views

urlpatterns = [
    path('debit/' ,views.debit_amount),
    path('credit/' ,views.credit_amount)
]