from django.urls import path
from . import views

urlpatterns = [
    path('app2/', views.app2, name='app2'),
]