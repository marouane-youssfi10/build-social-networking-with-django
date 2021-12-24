from django.shortcuts import render, redirect
from ask_questions.models import Ask_questions
# pagination
from django.core.paginator import Paginator

def home(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index')

    questions = Ask_questions.objects.all()

    # for questions page
    paginator_question = Paginator(questions, 5)
    page_number_question = request.GET.get('page')
    page_question = paginator_question.get_page(page_number_question)

    context = {
        'questions': page_question
    }

    return render(request, 'home.html', context)
