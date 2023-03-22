from rest_framework.routers import DefaultRouter

from classroom.views.model_view_set import *

router = DefaultRouter()

router.register(r'buildings', BuildingsModelViewSet, basename='buildings')
router.register(r'reservations', ReservationsModelViewSet, basename='reservations')
router.register(r'halls', HallsModelViewSet, basename='halls')
router.register(r'schools', SchoolsModelViewSet, basename='schools')
router.register(r'universities', UniversitiesModelViewSet, basename='universities')
router.register(r'departments', DepartmentsModelViewSet, basename='departments')

urlpatterns = router.urls
