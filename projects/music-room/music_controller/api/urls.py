
from django.urls import path
#include the views function to show the response in these endpoint urls
from .views import main

urlpatterns = [
    #if we get a url that is blank, call the main function from views
    #and this main function will do whatever we put in it 
    path('hello', main)
]
