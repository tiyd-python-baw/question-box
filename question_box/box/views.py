from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answers.objects.filter(question=question).all()
    return render (request, 'question_detail.html', {'question':question,
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
