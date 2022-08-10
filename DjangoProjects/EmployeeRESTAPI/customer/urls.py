from django.contrib import admin
from django.urls import path
from customer import views
from .views import (StudentApiView)

urlpatterns = [
   # path('getEmployees/',views.get_employee_details),
    path('getStudents/',StudentApiView.as_view()),
    path('getStudents/<int:student_id>/',StudentApiView.as_view()),
]