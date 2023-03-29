import secrets
from datetime import timedelta

from django.contrib.auth import authenticate
from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.views import TokenView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from classroom.serializers.auth_serializers import *


class LoginView(APIView, TokenView):
    serializer_class = LoginSerializer
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [AllowAny, ]

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    @swagger_auto_schema(
        operation_id="Login",
        operation_summary="Login a user",
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
        expiration_time = now() + timedelta(hours=6)
        user = authenticate(
            email=data.get('email'),
            password=data.get('password')
        )

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            application = Application.objects.get(name='Default')
            access_token = AccessToken.objects.create(
                user=user,
                application=application,
                expires=expiration_time,
                token=secrets.token_hex(16)
            )
            success_message = "User logged in successfully"

        response_data = {
            'success_message': success_message,
            'access_token': access_token.token,
            'token_type': 'Bearer',
            "expires_in": f'{(expiration_time - now()).seconds // 3600} hours',
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": f"{user.first_name} {user.last_name}",
                "user_type": str(user.get_user_role())
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        operation_id="Change Password",
        operation_summary="Change a user's password",
        operation_description="Change a user password",
        request_body=ChangePasswordSerializer,
        responses={
            200: "Password changed successfully",
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
        user.set_password(data.get('new_password'))
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="Logout Current User",
        operation_description="Logout a user",
        responses={
            200: "User logged out",
            500: "Server Error",
        }
    )
    def post(self, request):
        user = request.user
        app = Application.objects.get(user=user)
        token = AccessToken.objects.get(user=user, application=app)
        token.delete()
        return Response({"message": "User logged out"})
