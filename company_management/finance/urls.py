from django.urls import path
from . import views

urlpatterns = [
    # Example path
    path('summary/', views.finance_summary, name='finance_summary'),
    path('payroll/', views.payroll_list, name='finance_summary'),
    path('expense/', views.expense_list, name='finance_summary'),
    path('invoice/', views.invoice_list, name='finance_summary'),
    
]
