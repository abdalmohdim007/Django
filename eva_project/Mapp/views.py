from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Mapp(request):
    return HttpResponse("Hello Mohammed!")

def members(request):
  template = loader.get_template('mo.html')
  return HttpResponse(template.render(  request))
