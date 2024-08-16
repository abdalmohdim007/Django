from django.urls import path
from . import views

urlpatterns = [
    # Example path
    path('profile/', views.profile_list, name='profile'),
    path('performance/', views.performance_review_list, name='performance'),
    
]
