from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app4(request):
    return HttpResponse("Hello world!")

def app1(request):
  help_dict = {'help_me':"Hello I am from Help"}
  template = loader.get_template('app4/tests.html')
  return HttpResponse(template.render(help_dict, request))

def help(request):
  help_dict = {'help_abood':"Hello I am from Help  Me Abood"}
  template = loader.get_template('tests.html')
  return HttpResponse(template.render(help_dict, request))  