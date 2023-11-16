from django.urls import path

from .views import GeneratePdfFromSourceView

urlpatterns = [
    path("generate-pdf/", GeneratePdfFromSourceView.as_view(), name="generate-pdf"),
]
