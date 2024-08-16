from django import forms
from .models import companydb


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_company = forms.CharField(label="Your Company", max_length=100)
    your_department = forms.CharField(label="Your Department", max_length=100)
    your_salary = forms.CharField(label="Your Salary", max_length=100)
    your_employeeID = forms.CharField(label="Your employeeID", max_length=100)
   
class CompanyForm(forms.ModelForm):
     class Meta:
        model = companydb
        fields = '__all__'

     