from django.contrib import admin
from django.urls import include, path
from src.routes import routes

from .yasg import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(routes)),
    path(
        "swagger/",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
]
