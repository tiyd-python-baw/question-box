from django import forms
from .models import Question, Tag


class NewQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text','tags')
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
