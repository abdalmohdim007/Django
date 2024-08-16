from django.urls import path
from . import views

urlpatterns = [
    path('Mapp/', views.Mapp, name='Mapp'),
]