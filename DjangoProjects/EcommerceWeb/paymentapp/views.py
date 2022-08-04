from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def debit_amount(request):
    return HttpResponse("Hi, your account has been debited with 1000")

def credit_amount(request):
    return HttpResponse("Hi, your account has been credited with 1000")
