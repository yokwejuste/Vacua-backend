from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from classroom.models import Halls, Reservations
from classroom.serializers import *


# a get method to query all the free halls

class HallsView(generics.ListAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

    def get_queryset(self):
        queryset = Halls.objects.all().filter(status=True)
        hall_name = self.request.query_params.get('hall_name', None)
        if hall_name is not None:
            queryset = queryset.filter(hall_name__icontains=hall_name)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class LastHallReservationView(generics.RetrieveAPIView):
    serializer_class = ReservationsSerializer

    def get_queryset(self):
        queryset = Reservations.objects.all().filter(reserved_by=self.request.user).order_by('-created_at')
        return queryset

    @swagger_auto_schema(
        operation_id="Get last hall reservation",
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset[0]).data, status=status.HTTP_200_OK)


class GetOccupiedHallsView(generics.ListAPIView):
    serializer_class = HallsSerializer

    def get_queryset(self):
        queryset = Halls.objects.all().filter(status=True)
        return queryset

    @swagger_auto_schema(
        operation_id="Get occupied halls",
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(status=True)
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
