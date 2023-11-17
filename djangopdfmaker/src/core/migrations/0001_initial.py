# Generated by Django 4.2.7 on 2023-11-16 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "IN PROGRESS"),
                            ("completed", "COMPLETED"),
                            ("error", "ERROR"),
                        ],
                        db_index=True,
                        default="in_progress",
                        max_length=20,
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                (
                    "html_file",
                    models.FileField(
                        blank=True, null=True, upload_to="media/html_files/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeneratedPDF",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pdf_file", models.FileField(upload_to="media/generated_pdfs/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "task",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.task",
                    ),
                ),
            ],
        ),
    ]
