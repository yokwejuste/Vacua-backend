from django.db import models

from classroom.models import VacuaBaseModel, Schools


class Department(VacuaBaseModel):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(Schools, related_name='departments', on_delete=models.CASCADE, null=True, blank=True)
    hod = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name='Head of Department')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
