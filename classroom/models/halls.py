from django.db import models

from classroom.models.base_model import VacuaBaseModel


class Halls(VacuaBaseModel):
    building = models.ForeignKey('Buildings', on_delete=models.CASCADE)
    school = models.ForeignKey('Schools', on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    capacity = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Hall"
        verbose_name_plural = "Halls"

    def __str__(self):
        return self.name
