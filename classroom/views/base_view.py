from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class TestView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="This is a test endpoint",
        responses={
            200: "OK",
        }
    )
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "message": "Hello World"
            }
        )
