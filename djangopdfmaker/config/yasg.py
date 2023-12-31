from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Pdf Maker Api",
        default_version="v0.0.1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    urlconf="config.urls",
)
