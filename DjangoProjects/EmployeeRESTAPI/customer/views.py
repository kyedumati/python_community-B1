from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_employee_details(request):
    rollno = 1234
    name = "Ravi"
    marks = 100
    my_dict = {"rollno": rollno, "name": name, "marks": marks}
    return JsonResponse(my_dict)