from django.template import loader
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import EA

def app2(request):
  mymembers = EA.objects.all().values()
  template = loader.get_template('ea.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request)) 