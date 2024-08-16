from django.shortcuts import render
from .models import Profile, PerformanceReview

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'employees/profile_list.html', {'profiles': profiles})

def performance_review_list(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'employees/performance_review_list.html', {'reviews': reviews})
