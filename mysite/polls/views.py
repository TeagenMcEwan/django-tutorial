from django.shortcuts import render
from django.http import HttpResponse

# Create code here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    

