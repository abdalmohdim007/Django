from django.shortcuts import render
from .models import Question
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Answer
from django.contrib.auth.decorators import login_required



@login_required
def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})
def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})




def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        total = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):
                total += 1
                answer = Answer.objects.get(id=value)
                if answer.is_correct:
                    score += 1
        return HttpResponse(f'Your score: {score}/{total}')
    return redirect('quiz')

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "quiz/index.html", context)
