from django.shortcuts import render
from django.http import HttpResponse

"""
what is views ?
    It returns some page when the users request 
    It is a python function that accepts request from the user
    and then provides information
    
"""

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is homepage</h1>")
