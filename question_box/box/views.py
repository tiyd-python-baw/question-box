from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Question, Answers, Score
from .forms import NewQuestion
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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


def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answers.objects.filter(question=question).all()
    return render(request, 'question_detail.html', {'question': question,
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
            #return redirect('home_page', request.user.username)

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
