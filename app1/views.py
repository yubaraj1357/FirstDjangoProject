from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def yuvraj(request):
    return HttpResponse('<marquee><h2>yuvraj is future king</h2></marquee>')