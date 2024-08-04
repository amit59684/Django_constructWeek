from django import forms
from .models import Task, StudySession

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']

class StudySessionForm(forms.ModelForm):
    duration = forms.IntegerField(help_text="Duration in minutes")

    class Meta:
        model = StudySession
        fields = ['task', 'duration']
