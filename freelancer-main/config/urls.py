from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Freelancer API",
        default_version='v1',
        description="Freelancer loyiha API hujjati",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('backend.users.urls')),
    path('orders/', include('backend.orders.urls')),
    path('review/', include('backend.review.urls')),
    path('notification/', include('backend.notification.urls')),
    path('freelancerprofil/', include('backend.freelancerprofil.urls')),
    path('transactions/', include('backend.transactions.urls')),
    path('chatmessage/', include('backend.chatmessage.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)