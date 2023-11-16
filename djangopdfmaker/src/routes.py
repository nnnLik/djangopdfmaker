from django.urls import include, path

routes = [
    path("core/", include("src.core.urls"), name="core"),
]
