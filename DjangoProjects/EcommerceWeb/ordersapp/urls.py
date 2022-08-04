from django.contrib import admin
from django.urls import path
from ordersapp import views


urlpatterns = [
    path('display/',views.display_message),
    path('showtime/',views.time_view),
]