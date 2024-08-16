from django.http import HttpResponse
from django.template import loader
from .models import Member

def app1(request):
  help_dict = {'help_me':"Hello I am from Help Please 2"}
  template = loader.get_template('app1/test.html')
  return HttpResponse(template.render(help_dict, request))

def help(request):
    
    abood_dict = {'abood_me':"Hello I am from Help"}
    template = loader.get_template("app1/help.html")
    return HttpResponse(template.render(abood_dict, request)) 

def data(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('app1/data.html')  
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request)) 

