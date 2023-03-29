from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from classroom.models import *
from classroom.permissions import IsClassCoordinator, IsAdmin
from classroom.serializers import *


class BuildingsModelViewSet(ModelViewSet):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = BuildingsSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Buildings.objects.all()

    def get_queryset(self):
        return Buildings.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
 

class ReservationsModelViewSet(ModelViewSet):
    authentication_classes = [OAuth2Authentication, ]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    permission_classes = [IsAuthenticated, IsClassCoordinator, IsAdmin]

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
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [IsAuthenticated]
    serializer_class = HallsSerializer
    queryset = Halls.objects.all()

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
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = SchoolsSerializer
    queryset = Schools.objects.all()

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
    authentication_classes = [OAuth2Authentication, ]
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        return Schools.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
