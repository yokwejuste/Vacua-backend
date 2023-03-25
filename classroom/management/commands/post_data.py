import uuid

from django.core.management.base import BaseCommand

from classroom.models import *
from pre_data.data import SCHOOLS, DEPARTMENT

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


def truncate_db():
    Schools.objects.all().delete()
    Department.objects.all().delete()
    Users.objects.all().delete()
    Reservations.objects.all().delete()
    Buildings.objects.all().delete()
    Halls.objects.all().delete()


def school_id():
    return uuid.uuid4()


def department_id():
    return uuid.uuid4()


def get_school_name(school):
    return school['name']


class Command(BaseCommand):
    help = 'Load pre-data from a JSON file and write it to the Class model in the database.'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--only', type=str, help="Only")
        parser.add_argument('--mode', type=str, help="Mode")

    def run_schools_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Schools Seeder...'))
        for school in SCHOOLS:
            Schools.objects.create(
                id=school_id(),
                **school
            )

    def department_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Department Seeder...'))
        for department in DEPARTMENT:
            Department.objects.create(
                id=department_id(),
                school=Schools.objects.get(name=get_school_name(department['school'])),
                **department
            )

    def handle(self, *args, **options):
        if options['mode'] == MODE_CLEAR:
            truncate_db()
            self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
        elif options['mode'] == MODE_REFRESH:
            truncate_db()
            self.stdout.write(self.style.SUCCESS('Database refreshed successfully!'))
        else:
            self.stdout.write(self.style.WARNING('No mode selected!'))

        if options['only'] == 'schools':
            self.run_schools_seeder()
            self.stdout.write(self.style.SUCCESS('Schools seeded successfully!'))
        elif options['only'] == 'department':
            self.department_seeder()
            self.stdout.write(self.style.SUCCESS('Department seeded successfully!'))
        elif options['only'] == 'users':
            self.stdout.write(self.style.SUCCESS('Users seeded successfully!'))
        elif options['only'] == 'reservations':
            self.stdout.write(self.style.SUCCESS('Reservations seeded successfully!'))
        elif options['only'] == 'buildings':
            self.stdout.write(self.style.SUCCESS('Buildings seeded successfully!'))

        truncate_db()

        self.run_schools_seeder()

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
