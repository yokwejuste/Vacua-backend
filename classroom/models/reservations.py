from django.db import models

from classroom.models import VacuaBaseModel
from classroom.models.users import Users
from classroom.utils import get_current_user


class Reservations(VacuaBaseModel):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(Users, on_delete=models.CASCADE, default=get_current_user)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return self.status
