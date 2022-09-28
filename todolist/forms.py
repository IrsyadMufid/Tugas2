from django import forms
from todolist.models import Task

class CreateForm(forms.Form):
    title = forms.CharField(label = "Title")
    description = forms.CharField(label = "Description")