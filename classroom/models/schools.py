from django.db import models

from classroom.models import VacuaBaseModel


class Schools(VacuaBaseModel):
    director = models.CharField(max_length=35)
    name = models.CharField(max_length=35, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
