from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from classroom.models import Reservations, Schools
from classroom.models.buildings import Buildings
from classroom.models.halls import Halls
from classroom.serializers.buildings_serilizers import BuildingsSerializer
from classroom.serializers.departments_serializers import DepartmentSerializer
from classroom.serializers.halls_serializers import HallsSerializer
from classroom.serializers.reservation_serializers import ReservationsSerializer
from classroom.serializers.schools_serializers import SchoolsSerializer
from firebase_config import db as firebase_db


class BuildingsModelViewSet(ModelViewSet):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return firebase_db.collection('buildings').get()

    def perform_create(self, serializer):
        firebase_db.collection('buildings').push(serializer.data)
        return JsonResponse(serializer.data, status=201)

    def perform_update(self, serializer):
        firebase_db.collection('buildings').push(serializer.data)
        return JsonResponse(serializer.data, status=200)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class ReservationsModelViewSet(ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservations.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class HallsModelViewSet(ModelViewSet):
    serializer_class = HallsSerializer
    queryset = Halls.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Halls.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class SchoolsModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer

    def get_queryset(self):
        return Schools.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class UniversitiesModelViewSet(ModelViewSet):
    serializer_class = SchoolsSerializer
    queryset = Schools.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schools.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class DepartmentsModelViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Schools.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schools.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()