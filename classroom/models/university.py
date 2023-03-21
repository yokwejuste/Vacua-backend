from django.db import models

from classroom.models import VacuaBaseModel, Schools


class University(VacuaBaseModel):
    name = models.CharField(max_length=35)
    status = models.BooleanField(default=True)
    vice_chancellor = models.CharField(max_length=35)
    all_schools = models.ManyToManyField(Schools, related_name='universities', verbose_name='schools')
    town = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    g_map_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"
