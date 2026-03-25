from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    temp = "Temp Value"
    context = {'temp' : temp}
    return HttpResponse(template.render(context, request))