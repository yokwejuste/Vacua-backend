from django.core.management.base import BaseCommand
from oauth2_provider.models import Application

from classroom.models import *

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


def truncate_db():
    Schools.objects.all().delete()
    Department.objects.all().delete()
    Users.objects.all().delete()
    Reservations.objects.all().delete()
    Buildings.objects.all().delete()
    Halls.objects.all().delete()


class Command(BaseCommand):
    help = 'Load pre-data from a JSON file and write it to the Class model in the database.'

    def run_application_seeder(self):
        Application.objects.create(
            name="Default",
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )
        self.stdout.write(self.style.SUCCESS('Running Application Seeder...'))

    def add_arguments(self, parser):
        parser.add_argument('-o', '--only', type=str, help="Only")
        parser.add_argument('--mode', type=str, help="Mode")

    def run_schools_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Schools Seeder...'))
        school_1 = Schools.objects.create(
            name='School of Engineering',
            director='Dr. John Doe',
            symbol='SOE',
            status=True
        )
        school_1.save()
        school_2 = Schools.objects.create(
            name='School of Business',
            director='Alfred Johnson',
            symbol='SOB',
        )
        school_2.save()
        school_3 = Schools.objects.create(
            name='School of Law',
            director='Dr. Jane Doe',
            symbol='SOL',
        )
        school_3.save()

    def department_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Department Seeder...'))
        department_1 = Department.objects.create(
            name='Computer Science',
            school=Schools.objects.get(name='School of Engineering'),
            hod='Dr. John Doe',
        )
        department_1.save()
        department_2 = Department.objects.create(
            name='Electrical Engineering',
            school=Schools.objects.get(name='School of Engineering'),
            hod='Dr. Jane Doe',
        )
        department_2.save()
        department_3 = Department.objects.create(
            name='Mechanical Engineering',
            school=Schools.objects.get(name='School of Engineering'),
            hod='Dr. Bright Goodluck',
        )
        department_3.save()

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
        self.department_seeder()
        # check if application item with name 'Default' exists, if no create one else skip
        if not Application.objects.filter(name='Default').exists():
            self.run_application_seeder()
        self.stdout.write(self.style.SUCCESS('Application seeded successfully!'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
