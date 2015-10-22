from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answers, Score
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



# Create your views here.
def question_detail(request, question_pk):
    #question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    answers = Answers.objects.filter(question=question).all()
    return render (request, 'box/templates/question_detail.html', {'question':question,
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
