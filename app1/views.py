from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feature(request):
    return HttpResponse("ADD")