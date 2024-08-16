from django.urls import path
from . import views

urlpatterns = [
    path('Eapp/', views.Eapp, name='Eapp'),
]