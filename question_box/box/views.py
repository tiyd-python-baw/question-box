from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Question, Answers, Score
from .forms import NewQuestion
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from itertools import chain

from datetime import datetime


# Create your views here.

class UserPage(ListView):
    template_name = 'box/userpage.html'
    context_object_name = 'q_a'
    paginate_by = 20

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['pk'])
        self.points = self.user.score.points
        return sorted(chain(self.user.question_set.all(),self.user.answers_set.all()),key=lambda x: x.timestamp,reverse=True)


class AllQuestionsView(ListView):
    '''Used to list all questions on the Home page'''
    template_name = 'questionhome.html'
    context_object_name = 'questions'
    paginate_by = 20

    model = Question

    def get_queryset(self):
        preload = Question.objects.all()
        return preload.order_by('-timestamp')


def question_detail(request, question_pk):
    #question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    answers = Answers.objects.filter(question=question).order_by('-points_a').all()
    if request.method == 'POST':
        #if request.user.is_authenticated():
            vote = request.POST.get('vote', False)
            answer_text = request.POST.get('new_answer', False)
            if vote == 'upvote':
                answer = Answers.objects.get(pk=request.POST['answer_object'])
                answer.points_a +=1
                answer.save()
                answer.user.score.points +=10
                answer.user.score.save()
            elif vote =='downvote':
                answer = Answers.objects.get(pk=request.POST['answer_object'])
                answer.points_a -=1
                answer.save()
                answer.user.score.points -=5
                answer.user.score.save()
                #request.user.score.points -=1
                #request.user.score.save()
            else:
                new_answer = Answers(text=answer_text,
                                    timestamp=datetime.now(),
                                    question = question,
                                    user=request.user)
                new_answer.save()
            return render(request, 'box/question_detail.html', {'question':question,
                                                        'answers': answers})
    return render (request, 'box/question_detail.html', {'question':question,
                                                    'answers': answers})




def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            score = Score(user=user)
            score.save()
            user = authenticate(username=user.username,
                                password=request.POST['password1'])
            login(request, user)
            return redirect('home_page', request.user.username)

    else:
        form = UserCreationForm()
    return render(request, 'box/register.html', {'form': form})


@login_required
def new_question(request):
    form_class = NewQuestion

    if request.method == 'POST':     # want to post a new question
        form = form_class(data=request.POST)

        if form.is_valid():
            title = request.POST.get('title', '')
            text = request.POST.get('text', '')  # needs (commit=False)
#            user = request.user     # may be some magic here!

            question = Question(
                title=title,
                text=text
            )
            question.save()

            return redirect('newquestion')

    return render(request, 'box/newquestion.html', {'form': form_class})
