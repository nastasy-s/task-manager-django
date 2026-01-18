from django.contrib import admin
from .models import TaskType

# Register your models here.
@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
