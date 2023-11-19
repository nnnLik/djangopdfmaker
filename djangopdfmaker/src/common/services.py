import os

from django.utils import timezone
from src.core.models import Task


class CommonServices:
    def clean_old_files(self) -> None:
        one_week_ago = timezone.now() - timezone.timedelta(weeks=1)
        old_tasks = Task.objects.filter(created_at__lt=one_week_ago, is_deleted=False)

        for task in old_tasks:
            self._delete_generated_pdf(task)
            self._delete_html_file(task)
            self._update_task(task)

    def _delete_generated_pdf(self, task: Task) -> None:
        generated_pdf = task.generated_pdf
        if generated_pdf:
            self._delete_file(generated_pdf.pdf_file.path)
            generated_pdf.delete()

    def _delete_html_file(self, task: Task) -> None:
        if task.html_source_file:
            self._delete_file(task.html_source_file.path)

    def _update_task(self, task: Task) -> None:
        Task.objects.filter(pk=task.pk).update(
            html_source_file=None,
            source_url=None,
            is_deleted=True,
        )

    def _delete_file(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)


services: CommonServices = CommonServices()
