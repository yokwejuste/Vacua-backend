from datetime import datetime

from classroom.models import Reservations
from vacua.settings import env


def send_notification(reservation_id):
    # Retrieve the reservation object
    reservation = Reservations.objects.get(id=reservation_id)

    # Check if the current time is equal to the start time of the reservation
    current_time = datetime.now().time()
    if current_time != reservation.start_time:
        return

    # Construct the notification payload
    payload = {
        'to': reservation.reserved_by.phone_number if reservation.reserved_by.phone_number != '' else env(
            'TWILIO_TO_NUMBER'),
        'from': env('TWILIO_FROM_NUMBER'),
        'body': f"""
            Hello {reservation.reserved_by.first_name} {reservation.reserved_by.last_name},
            Your reservation for the hall {reservation.hall.name} has started at {reservation.start_time}.

            Details:
                Hall: {reservation.hall.name}
                Capacity: {reservation.hall.capacity}
                School: {reservation.hall.school.name}
                Building: {reservation.hall.building.name}

            With Care and Love,
            Vacua Team
        """
    }
