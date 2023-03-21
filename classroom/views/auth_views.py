from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from classroom.serializers.auth_serilizers import RegistrationSerializer


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=RegistrationSerializer,
        responses={
            200: "User created",
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(

            {

                "user": RegistrationSerializer(

                    serializer.instance, context=self.get_serializer_context()

                ).data,

            }

        )
