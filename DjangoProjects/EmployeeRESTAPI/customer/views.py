from django.shortcuts import render
from django.http import JsonResponse
from .dbconnect import *

# Create your views here.
# def get_employee_details(request):
# #     rollno = 1234
# #     name = "Ravi"
# #     marks = 100
# #     #my_dict = {"rollno": rollno, "name": name, "marks": marks}
# #     conn= getConnection()
# #     #preparing a cursor object
# #     cursorObject = conn.cursor()
# #     print("Displaying NAME and ROLL columns from the STUDENT table:")
# #     #selecting query
# #     query = "select FIRST_NAME,LAST_NAME,EMAIL_ID from python_community3.tbl_student_data"
# #     cursorObject.execute(query)
# #     myresult = cursorObject.fetchall()
# #     print(myresult)
# #     response=[]
# #     for x in myresult:
# #         record={"first_name":x[0],"last_name":x[1],"email_id":x[2]}
# #         response.append(record)
# #     print(myresult)
# #     #disconnecting from server
# #     conn.close()
# #     return JsonResponse(response,safe=False)
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentApiView(APIView):
    #get all the student info
    def get(self,request,*args,**kwargs):
        student_data=Student.objects.all()
        serializer=StudentSerializer(student_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #Create
    def post(self,request,*args,**kwargs):
        data ={
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "email_id": request.data.get('email_id')
        }
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    # Update
    def put(self, request,student_id, *args, **kwargs):
        student_instance=None
        try:
            student_instance = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            pass
        if not student_instance:
            return Response({"rest":"No student matching with given id"},status=status.HTTP_400_BAD_REQUEST)

        data = {
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "id": student_id
        }

        serializer = StudentSerializer(instance=student_instance,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update
    def delete(self, request,student_id, *args, **kwargs):
        try:
            student_instance= Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            pass
        if not student_instance:
            return Response({"rest":"No student matching with given id"},status=status.HTTP_400_BAD_REQUEST)


        student_instance.delete()    # delete from student where id=1

        return Response({"res":"Object deleted"}, status=status.HTTP_200_OK)



