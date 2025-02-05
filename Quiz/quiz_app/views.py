from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Question, Answer
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

@login_required
def quiz_view(request):
    """ Display the quiz questions """
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def submit_quiz(request):
    """ Process quiz submission and redirect to results page """
    if request.method == 'POST':
        score = 0
        total = 0

        for key, value in request.POST.items():
            if key.startswith('question_'):
                total += 1
                answer = Answer.objects.get(id=value)
                if answer.is_correct:
                    score += 1
        
        # Redirect to results page with score details
        return redirect('quiz_results', score=score, total=total)

    return redirect('quiz_home')

def results_page(request, score, total):
    """ Display the quiz results page """
    return render(request, 'quiz/results.html', {'score': score, 'total': total})

def send_mail_page(request):
    """ Handle sending emails from the quiz page """
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


from django.shortcuts import render

def about_view(request):
    return render(request, 'quiz/about.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject=f"New Contact Message from {name}",
            message=message,
            from_email=email,
            recipient_list=['your-email@example.com'],  # Change this to your email
        )

        messages.success(request, "Your message has been sent! ✅")
        return render(request, 'contact.html')

    return render(request, 'contact.html')