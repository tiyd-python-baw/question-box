from django.shortcuts import render

# Create your views here.
def question_detail(request, question_id):
    return render (request, 'question_detail.html')
