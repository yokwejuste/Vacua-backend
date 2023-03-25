import uuid
from datetime import datetime


def create_primary_key():
    return uuid.uuid4()


def get_first_related_model(model):
    return model.objects.first()


def get_current_user(request):
    return request.user


def convert_timestamp(timestamp):
    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f %z')
    return dt.strftime('%d/%m/%Y - %H:%M')
