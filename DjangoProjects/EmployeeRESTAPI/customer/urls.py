from django.contrib import admin
from django.urls import path
from customer import views


urlpatterns = [
    path('getEmployees/',views.get_employee_details),
]