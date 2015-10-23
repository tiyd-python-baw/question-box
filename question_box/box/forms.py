from django import forms
from .models import Question


class NewQuestion(forms.Form):
    '''Form for adding a new question'''
    title = forms.CharField(max_length=255)
    text = forms.TextField(max_length=1000, commit=False)

    class Meta:
        model = Question
        fields = ('title', 'text')
