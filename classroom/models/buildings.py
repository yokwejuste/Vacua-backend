from django.db import models

from classroom.models import VacuaBaseModel


class Buildings(VacuaBaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    g_map_link = models.CharField(max_length=255, verbose_name='Google Map Link')
    name = models.CharField(max_length=35, verbose_name='Building Name')
    number_of_halls = models.PositiveIntegerField(verbose_name='Number of Halls')
    school = models.ForeignKey('Schools', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
