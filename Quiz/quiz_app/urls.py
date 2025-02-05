from django.urls import path
from . import views
from .views import submit_quiz, results_page, about_view, contact_view

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('submit/', submit_quiz, name='submit_quiz'),  # Quiz submission
    path('results/<int:score>/<int:total>/', results_page, name='quiz_results'),  # Fix: Added <int:score> and <int:total>
    path("results/", results_page, name="quiz_results"),  # Results page route
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]