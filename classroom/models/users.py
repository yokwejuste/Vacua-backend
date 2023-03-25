from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from classroom.models import VacuaBaseModel
from classroom.utils import create_primary_key

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
    ('X', 'prefer not to say')
)

LEVEL_CHOICES = (
    (200, 'level 1'),
    (300, 'level 2'),
    (400, 'level 3'),
    (500, 'level 4'),
    (600, 'level 5')
)


class UserManager(BaseUserManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def create_user(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have an email')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Users(AbstractBaseUser, VacuaBaseModel):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER_CHOICES, default='X')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=20, null=True, blank=True, choices=LEVEL_CHOICES, default='O')
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    number_of_students = models.PositiveIntegerField(null=True, blank=True, default=0)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_assistant = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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

    def set_user_status(self, status):
        self.is_active = status
        self.save()

    class Meta:
        db_table = 'users'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
