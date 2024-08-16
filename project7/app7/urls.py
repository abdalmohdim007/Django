from django.urls import path
from . import views

urlpatterns = [
    path('app7/', views.app7, name='app7'),
     path('stars/', views.members, name='members'),
]