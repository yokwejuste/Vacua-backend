from django.db import models

from classroom.models import VacuaBaseModel


class Halls(VacuaBaseModel):
    building = models.ForeignKey('Buildings', on_delete=models.CASCADE)
    school = models.ForeignKey('Schools', on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    capacity = models.PositiveIntegerField()
    status = models.BooleanField(default=False)  # True if the hall is busy, False if the hall is free

    class Meta:
        verbose_name = "Hall"
        verbose_name_plural = "Halls"

    def __str__(self):
        return f'The hall {self.name} in {self.building.name}'
