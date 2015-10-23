from django import forms
from .models import Question


class NewQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')
