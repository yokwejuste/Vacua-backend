# Generated by Django 4.1.7 on 2023-03-31 11:37

import classroom.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('X', 'prefer not to say')], default='X', max_length=20, null=True)),
                ('level', models.CharField(blank=True, choices=[(200, 'level 1'), (300, 'level 2'), (400, 'level 3'), (500, 'level 4'), (600, 'level 5')], max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_students', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('user_type', models.CharField(choices=[('HOD', 'Head Of Department'), ('CC', 'Class Coordinator'), ('DEAN', 'School Director'), ('STAFF', 'System Administrator'), ('SUPERUSER', 'Global Administrator')], default='CC', max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_cc', models.BooleanField(default=True)),
                ('is_hod', models.BooleanField(default=False)),
                ('is_director', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('g_map_link', models.CharField(max_length=255, verbose_name='Google Map Link')),
                ('name', models.CharField(max_length=35, verbose_name='Building Name')),
                ('number_of_halls', models.PositiveIntegerField(verbose_name='Number of Halls')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
            },
        ),
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=35)),
                ('capacity', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.buildings')),
            ],
            options={
                'verbose_name': 'Hall',
                'verbose_name_plural': 'Halls',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('director', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=35, unique=True)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100)),
                ('course_lecturer', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.halls')),
                ('reserved_by', models.ForeignKey(default=classroom.utils.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.AddField(
            model_name='halls',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.schools'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(default=classroom.utils.create_primary_key, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('hod', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Head of Department')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='classroom.schools')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'departments',
            },
        ),
        migrations.AddField(
            model_name='buildings',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.schools'),
        ),
        migrations.AddField(
            model_name='users',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.department'),
        ),
        migrations.AddField(
            model_name='users',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.schools'),
        ),
    ]
