from django.db import models
from accounts.models import Worker


class TaskType(models.Model):
    name = models.CharField(
        max_length = 100,
        unique = True,
        verbose_name = "Task Type name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('urgent','Urgent'),
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]

    name = models.CharField(
        max_length = 200,
        verbose_name="Task Name"
    )

    description = models.TextField(
        blank = True,
        verbose_name="Description"
    )

    deadline =models.DateField(
        verbose_name="Deadline",
    )

    is_completed = models.BooleanField(
        default = False,
        verbose_name="Is completed",
    )

    priority = models.CharField(
        max_length = 10,
        choices = PRIORITY_CHOICES,
        verbose_name = "Priority",
        default='medium'
    )

    task_type = models.ForeignKey(
        TaskType,
        on_delete = models.CASCADE,
        verbose_name = "Task Type",
        related_name = 'task'
    )

    assignees = models.ManyToManyField(
        Worker,
        related_name = 'assigned_tasks',
        blank = True,
        verbose_name = "Assignees",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name = "Created at",
    )

    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated at",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['created_at']
