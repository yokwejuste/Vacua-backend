import uuid


def create_primary_key():
    return uuid.uuid4()


def get_first_related_model(model):
    return model.objects.first()


def get_current_user(request):
    return request.user

