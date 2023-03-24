import secrets
from datetime import timedelta

from django.contrib.auth import authenticate
from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.views import TokenView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from classroom.serializers.auth_serilizers import *


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=RegistrationSerializer,
        responses={
            200: RegistrationResponseSerializer(),
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


class LoginView(APIView, TokenView):
    serializer_class = LoginSerializer
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [AllowAny, ]

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    @swagger_auto_schema(
        operation_description="Login a user",
        request_body=LoginSerializer,
        responses={
            200: LoginResponseSerializer(),
            300: "Multiple choices",
            400: "Bad request",
            500: "Internal server error",
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = authenticate(
            email=data.get('email'),
            password=data.get('password')
        )

        application = Application.objects.get(name='Default')
        expiration_time = now() + timedelta(hours=6)
        access_token = AccessToken.objects.create(
            user=user, application=application,
            expires=expiration_time, token=secrets.token_hex(16)
        )
        access_token.user = user
        access_token.save()

        print(user)

        response_data = {
            'success_message': "User logged in successfully",
            'access_token': access_token.token,
            'token_type': 'Bearer',
            "expires_in": f'{(expiration_time - now()).seconds // 3600} hours',
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": f"{user.first_name} {user.last_name}",
                "is_assistant": user.is_assistant,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = LogoutSerializer
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        operation_description="Logout a user",
        responses={
            200: "User logged out",
        }
    )
    def post(self, request):
        user = request.user
        app = Application.objects.get(user=user)
        token = AccessToken.objects.get(user=user, application=app)
        token.delete()
        return Response({"message": "User logged out"})
