from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from classroom.permissions import *
from classroom.serializers.auth_serializers import *


class HodRegistrationView(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = HodRegistrationSerializer
    permission_classes = [IsAdminUser, IsDirector, IsAdmin]

    @swagger_auto_schema(
        operation_id="Register a Hod",
        operation_summary="Register a new Head of department",
        operation_description="Register a new Head of department",
        request_body=HodRegistrationSerializer,
        responses={
            200: HodRegistrationResponseSerializer(),
            300: "Multiple choices",
            400: "Bad request",
            500: "Internal server error",
        }
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response_data = {
            "user": serializer.data,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class HodUpdateUserView(generics.GenericAPIView):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = HodUpdateUserSerializer
    permission_classes = [IsAdminUser, IsDirector, IsAdmin, IsHOD]

    @swagger_auto_schema(
        operation_id="Update Hod Data",
        operation_summary="Update a Hod user data",
        operation_description="Update a Hod user data",
        request_body=HodUpdateUserSerializer,
        responses={
            200: HodUpdateUserSerializerResponse(),
            300: "Multiple choices",
            400: "Bad request",
            500: "Internal server error",
        }
    )
    def patch(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email = data.get('email')
        user.save()
        response_data = {
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": f"{user.first_name} {user.last_name}",
                "user_type": str(user.get_user_role())
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
