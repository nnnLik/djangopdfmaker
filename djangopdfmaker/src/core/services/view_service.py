from typing import Tuple, Union

from django.core.files.uploadedfile import InMemoryUploadedFile
from src.core.tasks.to_pdf import process_to_pdf

from ..models import Task


class ViewServices:
    def generate_pdf_from_source(
        self, to_pdf: Union[str, InMemoryUploadedFile], content_type: str
    ) -> Tuple[int, str]:
        task_obj = self._create_task(to_pdf, content_type)
        task_id = task_obj.id

        to_pdf_validated = (
            to_pdf if isinstance(to_pdf, str) else task_obj.html_file.path
        )

        process_to_pdf.delay(task_id, content_type, to_pdf_validated)

        return (task_id, "Processing started.")

    def _create_task(self, to_pdf: str, content_type: str) -> Task:
        return Task.objects.create(
            url=to_pdf if content_type == "url" else None,
            html_file=to_pdf if content_type == "file" else None,
            # user=... # TODO
        )


view_services: ViewServices = ViewServices()
