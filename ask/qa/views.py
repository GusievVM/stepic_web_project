from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def someview(request, *args, **kwargs):
    return HttpResponse("Rango says hey there world!")
#return HttpResponse('OK')
