import uuid
from datetime import datetime


def create_primary_key():
    return str(uuid.uuid4())


def get_first_related_model(model):
    return model.objects.first()


def get_current_user(request):
    return request.user


def convert_timestamp(timestamp):
    dt_obj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f%z')
    formatted_date = dt_obj.strftime('%d/%m/%Y - %H:%M')
    return formatted_date
