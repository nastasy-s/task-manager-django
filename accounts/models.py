from django.db import models

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
