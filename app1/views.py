from django.shortcuts import render
from django.http import HttpResponse
print("This is my 1st oage")
# Create your views here.
def feature(request):
    return HttpResponse("ADD")