from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django_q.tasks import async_task
from twilio.rest import Client

from classroom.models import VacuaBaseModel
from classroom.models.users import Users
from classroom.utils import get_current_user, convert_timestamp
from vacua.settings import env

client = Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN'))


class Reservations(VacuaBaseModel):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(Users, on_delete=models.CASCADE, default=get_current_user)
    hall = models.ForeignKey('Halls', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def save(self, *args, **kwargs):
        if self.start_time <= timezone.now() <= self.end_time:
            client.messages.create(
                to=self.reserved_by.phone_number if self.reserved_by.phone_number != '' else env('TWILIO_TO_NUMBER'),
                from_=env('TWILIO_FROM_NUMBER'),
                body=f"""
                Hello {self.reserved_by.first_name} {self.reserved_by.last_name},
                Your reservation for the hall {self.hall.name} has been confirmed for {convert_timestamp(self.date)} \
                from {convert_timestamp(self.start_time)} to {convert_timestamp(self.end_time)}.
                
                
                Details:
                    Hall: {self.hall.name}
                    Capacity: {self.hall.capacity}
                    School: {self.hall.school.name}
                    Building: {self.hall.building.name}
                    
                
                With Care and Love,
                Vacua Team
                """
            )
            self.status = True
        else:
            self.status = False

        scheduled_time = datetime.combine(self.date, self.start_time)
        async_task('classroom.tasks.send_notification', reservation_id=self.id, schedule=scheduled_time)

    def __str__(self):
        return f'Reservation for {self.hall.name} by \
        {self.reserved_by.first_name} {self.reserved_by.last_name}'


@receiver(post_save, sender=Reservations)
async def update_hall_status(sender, instance, **kwargs):
    if instance.start_time <= timezone.now() <= instance.end_time:
        client.messages.create(
            to=instance.reserved_by.phone_number if instance.reserved_by.phone_number != '' else env(
                'TWILIO_TO_NUMBER'),
            from_=env('TWILIO_FROM_NUMBER'),
            body=f"""
            Hey {instance.reserved_by.first_name} {instance.reserved_by.last_name},
            
            You reserved the hall {instance.hall.name} for {instance.date} from {instance.start_time} to {instance.end_time}.
            
            Your reservation is confirmed and starts now.
            
            Time left: {instance.end_time - timezone.now()}
            
            Details:
                Hall: {instance.hall.name}
                Capacity: {instance.hall.capacity}
                School: {instance.hall.school.name}
                Building: {instance.hall.building.name}
            """
        )
        instance.status = True  # hall is occupied
    else:
        instance.status = False  # hall is free
    instance.save()
