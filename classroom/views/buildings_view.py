from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classroom.models.buildings import Buildings
from classroom.serializers.buildings_serilizers import BuildingsSerializer


class BuildingsView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="This endpoint returns a list of buildings",
        responses={
            200: "OK",
            202: "Accepted",
            400: "Bad Request",
        }
    )
    def get(self, request, *args, **kwargs):
        buildings = Buildings.objects.all()
        serializer = BuildingsSerializer(buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
