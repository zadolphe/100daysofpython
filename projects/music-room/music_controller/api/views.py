from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#write a functionn to take a reuqest and send to an endpoint to make a response to request
def main(request):
    return HttpResponse("<h1>hello, this is a paragraph<h1>") 