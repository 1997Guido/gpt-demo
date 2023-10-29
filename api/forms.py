from django import forms
from .models import QueryCategory

class QuestionForm(forms.Form):
    question = forms.CharField(label='Vraag', max_length=255)
    query_category = forms.ModelChoiceField(label='Vraagcategorie', queryset=QueryCategory.objects.all())
