from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def app7(request):
   pro7_dict = {'Stars_technology':"Hello I am from stars technology"}
   template = loader.get_template('pro7.html')
   return HttpResponse(template.render(pro7_dict, request))  


def members(request):
  pro7_dict = {'Stars_technology':"Hello I am from Help"}
  template = loader.get_template('pro7.html')
  return HttpResponse(template.render(pro7_dict, request))   