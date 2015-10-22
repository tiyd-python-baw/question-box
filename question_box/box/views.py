from django.shortcuts import render

# Create your views here.
def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answers.objects.filter(question=question).all()
    return render (request, 'question_detail.html', {'question':question,
                                                    'answers': answers})
