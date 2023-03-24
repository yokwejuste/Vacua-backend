from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Vacua API",
        default_version='v1',
        description="The API for the Vacua project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="yokwejuste@vacua.page"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^v1/api/console/', include(('classroom.urls.extra_routes', 'classroom'),
                                         namespace=f'extra_routers')),
    re_path(r'^v1/api/console/', include(('classroom.urls', 'classroom'), namespace=f'auth')),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
