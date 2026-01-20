from django import forms
from django.contrib.auth import get_user_model
from .models import Task, TaskType


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type', 'priority', 'deadline', 'assignees', 'is_completed']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'task_type': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'assignees': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
