from django.shortcuts import render
from .models import Question, Answers, Score
from django.views.generic.list import ListView


# Create your views here.

class AllQuestionsView(ListView):
    '''Used to list all questions on the Home page'''
    template_name = 'questionhome.html'
    context_object_name = 'questions'
    paginate_by = 20

    model = Question

    def get_queryset(self):
        preload = Question.objects.all()
        return preload.order_by('-timestamp')
