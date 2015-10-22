from django.shortcuts import render
from .models import Question, Answers, Score
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answers, Score
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



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


def question_detail(request, question_pk):
    #question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    answers = Answers.objects.filter(question=question).all()
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
            #return redirect('home_page', request.user.username)

    else:
        form = UserCreationForm()
    return render(request, 'box/register.html', {'form': form})
