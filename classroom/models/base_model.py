from django.db import models

from classroom.utils import create_primary_key


class VacuaBaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class VacuaBaseModelDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_deleted=False)


class VacuaBaseModel(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default=create_primary_key(), editable=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = VacuaBaseModelManager()

    deleted_objects = VacuaBaseModelDeleteManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_primary_key()
        super().save(*args, **kwargs)
