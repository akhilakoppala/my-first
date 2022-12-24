from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ashok(reuest):
    return HttpResponse('I am very hungry')


def aravind(request):
    return HttpResponse('<h1>my brother ashok</h1>')