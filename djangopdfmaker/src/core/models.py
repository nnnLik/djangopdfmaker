import uuid

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "IN PROGRESS"),
        ("completed", "COMPLETED"),
        ("error", "ERROR"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="in_progress", db_index=True
    )
    url = models.URLField(null=True, blank=True)
    html_file = models.FileField(upload_to="html_files/", null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task ({self.pk}) is {self.status}"


class GeneratedPDF(models.Model):
    pdf_file = models.FileField(upload_to="generated_pdfs/")
    task = models.OneToOneField(
        Task, null=True, on_delete=models.SET_NULL, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
