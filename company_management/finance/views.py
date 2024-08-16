from django.shortcuts import render
from .models import Payroll, Expense, Invoice

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'finance/payroll_list.html', {'payrolls': payrolls})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'finance/expense_list.html', {'expenses': expenses})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'finance/invoice_list.html', {'invoices': invoices})

def finance_summary(request):
    return render(request, 'finance/summary.html')
