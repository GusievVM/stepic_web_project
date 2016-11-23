from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse

from django.template import Context, loader

def someview(request, *args, **kwargs):
    return HttpResponse("Rango says hey there world!")
#return HttpResponse('OK')

def templatetestbase(request, *args, **kwargs):
    template = loader.get_template('qa/base.html')
    context = Context("Rango says hey there world!")

    return HttpResponse(template.render(context))

def templatetestindex(request, *args, **kwargs):
    template = loader.get_template('qa/index.html')
    context = Context("Rango says hey there world!")

    return HttpResponse(template.render(context))