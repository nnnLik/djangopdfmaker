import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
from src.common.enums import ContentType
from weasyprint import HTML

from ..models import GeneratedPDF, Task


class TaskServices:
    def process_html_to_pdf(
        self, task_id: int, content_type: ContentType, to_pdf: str
    ) -> None:
        try:
            match (content_type):
                case ContentType.URL:
                    pdf_content = self._generate_pdf_from_url(to_pdf)
                case ContentType.FILE:
                    pdf_content = self._generate_pdf_from_file_path(to_pdf)
                case _:
                    raise ValueError("Invalid source type.")

            pdf_path = self._save_pdf(pdf_content, task_id)
            self._change_status_to_comleted(task_id, pdf_path)
        except Exception as e:
            self._change_status_to_error(task_id, str(e))

    def _generate_pdf_from_url(self, url: str) -> str:
        try:
            response = requests.get(url)
            # TODO: do I need a status code check?
            pdf_content = HTML(string=response.text).write_pdf()
        except Exception as e:
            raise ValueError(f"Failed to generate PDF from URL: {e}.")

        return pdf_content

    def _generate_pdf_from_file_path(self, file_path: str) -> str:
        try:
            pdf_content = HTML(filename=file_path).write_pdf()
        except Exception as e:
            raise ValueError(f"Failed to generate PDF from file: {e}.")

        return pdf_content

    def _save_pdf(self, pdf_content: bytes, task_id: int) -> str:
        pdf_file_name = f"generated_pdfs/{task_id}.pdf"
        pdf_path = default_storage.save(pdf_file_name, ContentFile(pdf_content))
        return pdf_path

    @transaction.atomic
    def _change_status_to_comleted(self, task_id: int, pdf_path: str) -> None:
        generated_pdf = GeneratedPDF.objects.create(pdf_file=pdf_path)
        Task.objects.filter(id=task_id).update(
            generated_pdf=generated_pdf,
            status=Task.TaskStatus.COMPLETED,
            status_message="Task completed successfully.",
        )

    def _change_status_to_error(self, task_id: int, error_message: str) -> None:
        Task.objects.filter(id=task_id).update(
            status=Task.TaskStatus.ERROR, status_message=f"Error: {error_message}"
        )


task_services: TaskServices = TaskServices()
