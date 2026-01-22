from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type', 'priority', 'deadline', 'assignees', 'is_completed']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter task name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter task description'
            }),
            'task_type': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'date'
            }),
            'assignees': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '5'
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'name': 'Task Name',
            'description': 'Description',
            'task_type': 'Task Type',
            'priority': 'Priority',
            'deadline': 'Deadline',
            'assignees': 'Assignees',
            'is_completed': 'Mark as completed'
        }
