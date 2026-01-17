from django.db import models

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

