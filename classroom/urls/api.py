from django.urls import path, include, re_path
from classroom.views.auth_views import RegistrationView

urlpatterns = [
    re_path(r'auth/register', RegistrationView.as_view(), name='register'),
]
