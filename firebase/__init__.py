import os

import firebase_admin
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials, firestore
from rest_framework.authentication import BaseAuthentication

from exceptions import NoAuthToken, InvalidAuthToken, FirebaseError
from vacua.settings import BASE_DIR, env

cred = credentials.Certificate(os.path.join(BASE_DIR, env('GOOGLE_CREDENTIALS_FIREBASE')))
firebase_admin.initialize_app(cred)

firebase_db = firestore.client()


class Firebase:
    def __init__(self):
        self.db = firebase_db

    def get(self, collection, document):
        return self.db.collection(collection).document(document).get().to_dict()

    def get_all(self, collection):
        return self.db.collection(collection).get()

    def get_all_where(self, collection, field, operator, value):
        return self.db.collection(collection).where(field, operator, value).get()

    def get_all_where_in(self, collection, field, value):
        return self.db.collection(collection).where(field, 'in', value).get()

    def get_all_where_not_in(self, collection, field, value):
        return self.db.collection(collection).where(field, 'not-in', value).get()

    def get_all_where_array_contains(self, collection, field, value):
        return self.db.collection(collection).where(field, 'array-contains', value).get()

    def get_all_where_array_contains_any(self, collection, field, value):
        return self.db.collection(collection).where(field, 'array-contains-any', value).get()

    def get_all_where_not_equal(self, collection, field, value):
        return self.db.collection(collection).where(field, '!=', value).get()

    def get_all_where_greater_than(self, collection, field, value):
        return self.db.collection(collection).where(field, '>', value).get()

    def get_all_where_greater_than_or_equal(self, collection, field, value):
        return self.db.collection(collection).where(field, '>=', value).get()

    def get_all_where_less_than(self, collection, field, value):
        return self.db.collection(collection).where(field, '<', value).get()

    def get_all_where_less_than_or_equal(self, collection, field, value):
        return self.db.collection(collection).where(field, '<=', value).get()

    def get_all_where_order_by(self, collection, field, operator, value, order_by, order):
        return self.db.collection(collection).where(field, operator, value).order_by(order_by, order).get()

    def get_all_where_in_order_by(self, collection, field, value, order_by, order):
        return self.db.collection(collection).where(field, 'in', value).order_by(order_by, order).get()

    def get_all_where_not_in_order_by(self, collection, field, value, order_by, order):
        return self.db.collection(collection).where(field, 'not-in', value).order_by(order_by, order).get()

    def get_all_where_array_contains_order_by(self, collection, field, value, order_by, order):
        return self.db.collection(collection).where(field, 'array-contains', value).order_by(order_by, order).get()


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return user, None
