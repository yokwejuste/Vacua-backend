from django.db import models

from classroom.models import VacuaBaseModel
from classroom.models.halls import Halls


class Reservations(VacuaBaseModel):
    hall = models.ManyToManyField(Halls, related_name='reservations')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)
    reserved_by = models.CharField(max_length=35)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return self.hall.name
