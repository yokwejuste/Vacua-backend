from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
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

    def run_department_seeder(self):
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

    def run_building_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Building Seeder...'))
        building_1 = Buildings.objects.create(
            name='Engineering Building',
            latitude=12.345678,
            longitude=12.345678,
            number_of_halls=5,
            g_map_link='https://goo.gl/maps/1J1J1J1J1J1J1J1J1',
            school=Schools.objects.get(name='School of Engineering'),
        )
        building_1.save()
        building_2 = Buildings.objects.create(
            name='Business Building',
            latitude=12.345678,
            longitude=12.345678,
            number_of_halls=5,
            g_map_link='https://goo.gl/maps/1J1J1J1J1J1J1J1J1',
            school=Schools.objects.get(name='School of Business'),
        )
        building_2.save()
        building_3 = Buildings.objects.create(
            name='Law Building',
            latitude=12.345678,
            longitude=12.345678,
            number_of_halls=5,
            g_map_link='https://goo.gl/maps/1J1J1J1J1J1J1J1J1',
            school=Schools.objects.get(name='School of Law'),
        )
        building_3.save()

    def run_hall_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running Hall Seeder...'))
        hall_1 = Halls.objects.create(
            name='Engineering Hall 1',
            building=Buildings.objects.get(name='Engineering Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Engineering'),
        )
        hall_1.save()
        hall_2 = Halls.objects.create(
            name='Engineering Hall 2',
            building=Buildings.objects.get(name='Engineering Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Engineering'),
        )
        hall_2.save()
        hall_3 = Halls.objects.create(
            name='Engineering Hall 3',
            building=Buildings.objects.get(name='Engineering Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Engineering'),
        )
        hall_3.save()
        hall_4 = Halls.objects.create(
            name='Engineering Hall 4',
            building=Buildings.objects.get(name='Engineering Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Engineering'),
            status=True
        )
        hall_4.save()
        hall_5 = Halls.objects.create(
            name='Engineering Hall 5',
            building=Buildings.objects.get(name='Engineering Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Engineering'),
            status=True
        )
        hall_5.save()
        hall_6 = Halls.objects.create(
            name='Business Hall 1',
            building=Buildings.objects.get(name='Business Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Business'),
        )
        hall_6.save()
        hall_7 = Halls.objects.create(
            name='Business Hall 2',
            building=Buildings.objects.get(name='Business Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Business'),
        )
        hall_7.save()
        hall_8 = Halls.objects.create(
            name='Business Hall 3',
            building=Buildings.objects.get(name='Business Building'),
            capacity=200,
            school=Schools.objects.get(name='School of Business'),
        )
        hall_8.save()

    def run_reservation_seeder(self):

        self.stdout.write(self.style.SUCCESS('Running Reservation Seeder...'))
        reservation_1 = Reservations.objects.create(
            reserved_by=Users.objects.get(username='yokwejuste'),
            hall=Halls.objects.get(name='Engineering Hall 1'),
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(hours=2),
            course_name='Software Engineering',
            course_code='CSC 411',
            course_lecturer='Steve Brotherhood',
            date=timezone.now() + timedelta(days=3),
        )
        reservation_1.save()

    def run_user_seeder(self):
        self.stdout.write(self.style.SUCCESS('Running User Seeder...'))
        user_1 = Users.objects.create(
            username='etiane',
            email='etiane@vc.com',
            first_name='Etiane',
            last_name='Lenyuiy',

            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user_1.set_password('password')
        user_1.save()
        user_2 = Users.objects.create(
            username="yokwejuste",
            email="yokwejuste@vacua.page",
            first_name="Steve",
            last_name="Alonzo",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            phone_number="+237677123206"
        )
        user_2.set_password('password')
        user_2.save()

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
            self.run_department_seeder()
            self.stdout.write(self.style.SUCCESS('Department seeded successfully!'))
        elif options['only'] == 'users':
            self.stdout.write(self.style.SUCCESS('Users seeded successfully!'))
        elif options['only'] == 'reservations':
            self.stdout.write(self.style.SUCCESS('Reservations seeded successfully!'))
        elif options['only'] == 'buildings':
            self.stdout.write(self.style.SUCCESS('Buildings seeded successfully!'))

        truncate_db()
        self.run_user_seeder()
        self.run_schools_seeder()
        self.run_department_seeder()
        self.run_building_seeder()
        self.run_hall_seeder()
        self.run_reservation_seeder()
        # check if application item with name 'Default' exists, if no create one else skip
        if not Application.objects.filter(name='Default').exists():
            self.run_application_seeder()
        self.stdout.write(self.style.SUCCESS('Application seeded successfully!'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
