from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# Two types of views
# 1. Function based views
# 2. Class based views

# Display a text using view
def display_message(request):
    return HttpResponse("Hello Everyone, welcome to python world")

def time_view(request):
    time= datetime.datetime.now()
    s='<h1 style="color:green;">Hello Everyone, Current date and time is :'+ str(time)+'</h1>'

    s=s+'<table border="1" ><tr><td>Name</td><td>Address</td><td>Phone</td></tr><tr><td>Kasi</td><td>Ongole</td><td>6302193992</td></tr>' \
        '</table>'
    rollno=1234
    name="Ravi"
    marks=100
    my_dict = {"current_time": time,"rollno":rollno,"name":name,"marks":marks}
    return render(request,'showtime.html',context=my_dict)
    #return HttpResponse(s)

#Http code
#http methods

#static --> css,js,images
#templates --> html