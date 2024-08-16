from django.urls import path
from . import views

urlpatterns = [
   path('companylist', views.company_list, name='company_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('company/<int:pk>/update/', views.company_update, name='company_update'),
]