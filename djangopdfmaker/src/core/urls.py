from django.urls import path

from .views import GeneratePdfFromSourceView, TaskDetailsView

urlpatterns = [
    path("generate-pdf/", GeneratePdfFromSourceView.as_view(), name="generate-pdf"),
    path("tasks/<uuid:id>/", TaskDetailsView.as_view(), name="task-details"),
]
