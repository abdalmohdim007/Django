from django.urls import path
from . import views

urlpatterns = [
    path('app4/', views.app4, name='app4'),
    #path('app4/', views.Baba, name="Baba"),
]