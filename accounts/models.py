from django.db import models
from django.contrib.auth.models import AbstractUser

class Position(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Position name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers",
        verbose_name="Position"
    )

    def __srt__(self):
        return self.username

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
