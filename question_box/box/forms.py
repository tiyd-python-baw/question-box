from django import forms
from .models import Question


class NewQuestion(forms.Form):
    '''Form for adding a new question'''

    class Meta:
        model = Question
        fields = ('title', 'text')
