from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Employee, LeaveRequest, Attendance
from .forms import EmployeeForm, LeaveRequestForm, AttendanceForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


# Employee List, Add, Update, and Delete
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hr/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'hr/employee_confirm_delete.html', {'employee': employee})

def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'hr/leave_request_list.html', {'leave_requests': leave_requests})

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'hr/attendance_list.html', {'attendance_records': attendance_records})


def home(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'hr/attendance_list.html', {'attendance_records': attendance_records})
 

