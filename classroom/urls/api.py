from django.urls import re_path

from classroom.views.auth_views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    re_path(r'auth/register', RegistrationView.as_view(), name='register'),
    re_path(r'auth/login', LoginView.as_view(), name='login'),
    re_path(r'auth/logout', LogoutView.as_view(), name='logout'),
]
