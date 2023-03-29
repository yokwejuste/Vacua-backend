from rest_framework import generics

from classroom.models import Halls
from classroom.serializers import HallsSerializer


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