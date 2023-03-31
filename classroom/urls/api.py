from django.urls import re_path

from classroom.views import LastHallReservationView
from classroom.views.auth_views import *

urlpatterns = [
    # common paths
    re_path(r'auth/change_password', ChangePasswordView.as_view(), name='change_password'),
    re_path(r'auth/login', LoginView.as_view(), name='login'),
    re_path(r'auth/logout', LogoutView.as_view(), name='logout'),

    # Class coordinator authentication urls
    re_path(r'auth/cc/register', CCRegistrationView.as_view(), name='cc_register'),
    re_path(r'auth/cc/update', CCUpdateUserView.as_view(), name='cc_update'),

    # Head of department authentication urls
    re_path(r'auth/hod/register', HodRegistrationView.as_view(), name='hod_register'),
    re_path(r'auth/hod/update', HodUpdateUserView.as_view(), name='hod_update'),

    # Director of school authentication urls
    re_path(r'auth/dean/register', DeanRegistrationView.as_view(), name='dean_register'),
    re_path(r'auth/dean/update', DeanUpdateUserView.as_view(), name='dean_update'),

    # Query for last hall reservation
    re_path(r'reservations/last_reservation', LastHallReservationView.as_view(), name='hall_reservation'),
]
