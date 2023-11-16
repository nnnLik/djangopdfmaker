from django.contrib import admin

from .models import GeneratedPDF, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "url", "user", "created_at", "updated_at")
    list_filter = ("status", "user")
    search_fields = ("id", "url", "user__username", "user__email")
    date_hierarchy = "created_at"
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(GeneratedPDF)
class GeneratedPDFAdmin(admin.ModelAdmin):
    list_display = ("pdf_file", "task", "created_at")
    list_filter = ("task__status",)
    search_fields = ("pdf_file", "task__id")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
