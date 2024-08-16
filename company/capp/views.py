from django.template import loader
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import companydb
from .forms import NameForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CompanyForm

def capp(request):
    return HttpResponse("Hello world!")

def company(request):
    myemployees = companydb.objects.all().values()
    template = loader.get_template('company.html')
    context = {
    'myemployees':myemployees ,
  }
    return HttpResponse(template.render(context, request)) 
    

def department(request):
    myemployees = companydb.objects.all().values()
    template = loader.get_template('department.html')
    context = {
    'myemployees':myemployees ,
 }
    return HttpResponse(template.render(context, request)) 

def employee(request):
    myemployees = companydb.objects.all().values()
    template = loader.get_template('employee.html')
    context = {
    'myemployees':myemployees ,
 }
    return HttpResponse(template.render(context, request)) 

  

def thankyou(request):
    myemployees = companydb.objects.all().values()
    template = loader.get_template('thankyou.html')
    context = {
    'myemployees':myemployees ,
 }
    return HttpResponse(template.render(context, request)) 

def main(request):
    myemployees = companydb.objects.all().values()
    template = loader.get_template('main.html')
    context = {
    'myemployees':myemployees ,
 }
    return HttpResponse(template.render(context, request)) 

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("form.data your_name: ", form.data["your_name"])
            print("form.data your_company: ", form.data["your_company"])
            b = companydb(employee_firstname=form.data["your_name"],company=form.data["your_company"], 
                          department=form.data["your_department"],
                          salary=form.data["your_salary"],employeeID=form.data["your_employeeID"])
            b.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thankyou/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})

def company_list(request):
    companies = companydb.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(companydb, pk=pk)
    return render(request, 'company_detail.html', {'company': company})

def company_update(request, pk):
    company = get_object_or_404(companydb, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_update.html', {'form': form, 'company': company})

 