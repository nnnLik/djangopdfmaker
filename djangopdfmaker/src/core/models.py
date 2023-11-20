import uuid

from django.db import models
from src.common.utils import generate_unique_filename


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "IN PROGRESS"
        COMPLETED = "COMPLETED", "COMPLETED"
        ERROR = "ERROR", "ERROR"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.IN_PROGRESS,
        db_index=True,
    )
    status_message = models.TextField(null=True, blank=True)
    source_url = models.URLField(null=True, blank=True)
    html_source_file = models.FileField(
        upload_to=generate_unique_filename, null=True, blank=True
    )
    generated_pdf = models.OneToOneField(
        "GeneratedPDF", null=True, on_delete=models.SET_NULL, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return f"Task ({self.pk}) is {self.status}"


class GeneratedPDF(models.Model):
    pdf_file = models.FileField(upload_to="generated_pdfs/")
    created_at = models.DateTimeField(auto_now_add=True)
