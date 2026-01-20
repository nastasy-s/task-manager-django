from django.shortcuts import render, get_object_or_404
from .models import Task, TaskType
from accounts.models import Position

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)

def home(request):
    tasks = Task.objects.all()
    position_filter = request.GET.get('position')
    task_type_filter = request.GET.get('task_type')
    priority_filter = request.GET.get('priority')

    if position_filter:
        tasks = tasks.filter(assignees__position__=position_filter)

    if task_type_filter:
        tasks = tasks.filter(task_type__id=task_type_filter)

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()
    in_progress_tasks = total_tasks - completed_tasks

    positions = Position.objects.all()
    task_types = TaskType.objects.all()
    priorities = Task.PRIORITY_CHOICES

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'positions': positions,
        'task_types': task_types,
        'priorities': priorities,
        'current_position': position_filter,
        'current_task_type': task_type_filter,
        'current_priority': priority_filter,
    }

    return render(request, 'tasks/home.html', context)


def task_list(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)
