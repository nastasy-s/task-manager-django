from django.contrib import admin
from .models import TaskType, Task

# Register your models here.
@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'task_type',
        'priority',
        'deadline',
        'is_completed',
        'created_at'
    ]
    list_filter = ['task_type', 'priority', 'is_completed', 'deadline']
    search_fields = ['name', 'description']
    filter_horizontal = ['assignees']
    date_hierarchy = 'deadline'


    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'task_type')
        }),
        ('Schedule', {
            'fields': ('deadline', 'priority', 'is_completed')
        }),
        ('Assignment', {
            'fields': ('assignees',)
        }),
    )
