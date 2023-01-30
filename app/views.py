from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tejareddy(request,name):
    return HttpResponse(f' siri is bad girl  {name}')
