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