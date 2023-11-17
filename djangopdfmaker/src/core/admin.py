from django.contrib import admin

from .models import GeneratedPDF, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "source_url",
        "created_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = (
        "id",
        "source_url",
    )
    date_hierarchy = "created_at"
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )


@admin.register(GeneratedPDF)
class GeneratedPDFAdmin(admin.ModelAdmin):
    list_display = (
        "pdf_file",
        "created_at",
    )
    search_fields = ("pdf_file",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
