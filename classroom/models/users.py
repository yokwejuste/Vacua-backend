from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from classroom.models import VacuaBaseModel
from classroom.models.departments import Department
from classroom.utils import create_primary_key

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'other')
)

LEVEL_CHOICES = (
    (200, 'level 1'),
    (300, 'level 2'),
    (400, 'level 3'),
    (500, 'level 4'),
    (600, 'level 5')
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, VacuaBaseModel):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER_CHOICES, default='O')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True, choices=LEVEL_CHOICES, default='O')
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_primary_key()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
