from django.urls import path
from . import views

urlpatterns = [
    path('app1/', views.app1, name='app1'),
    #path('app1/', views.help, name="help"),
]