from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def maharaj(request):
    return HttpResponse('<marquee><h2>Maharaj is present king</h2></marquee>')
