from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('leave_requests/', views.leave_request_list, name='leave_request_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
