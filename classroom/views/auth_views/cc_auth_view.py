from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from classroom.permissions import *
from classroom.serializers.auth_serializers import *


class CCRegistrationView(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = CCRegistrationSerializer
    permission_classes = [IsAdminUser, IsAdmin, IsDirector, IsHOD]

    @swagger_auto_schema(
        operation_id="Register a CC",
        operation_summary="Register a new class coordinator",
        operation_description="Register a new class coordinator",
        request_body=CCRegistrationSerializer,
        responses={
            200: CCRegistrationResponseSerializer(),
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


class CCUpdateUserView(generics.GenericAPIView):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = CCUpdateUserSerializer
    permission_classes = [IsAdminUser, IsAdmin, IsDirector, IsHOD, IsClassCoordinator]

    @swagger_auto_schema(
        operation_id="Update CC Data",
        operation_summary="Update a CC user data",
        operation_description="Update a CC user data",
        request_body=CCUpdateUserSerializer,
        responses={
            200: CCUpdateUserSerializerResponse(),
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
