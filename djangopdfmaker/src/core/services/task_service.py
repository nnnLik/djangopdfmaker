import pdfkit
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from src.core.models import GeneratedPDF


class TaskServices:
    def process_html_to_pdf(self, task_id: int, type: str, to_pdf: str) -> None:
        match (type):
            case "url":
                pdf_content = self._generate_pdf_from_url(to_pdf)
            case "file":
                pdf_content = self._generate_pdf_from_file_path(to_pdf)
            case _:
                raise ValueError("Invalid source type.")

        pdf_path = self._save_pdf(pdf_content, task_id)

        GeneratedPDF.objects.create(pdf_file=pdf_path, task_id=task_id)

    def _generate_pdf_from_url(self, url: str) -> str:
        try:
            pdf_content = pdfkit.from_url(url, False)
        except Exception as e:
            raise ValueError(f"Failed to generate PDF from URL: {e}.")

        return pdf_content

    def _generate_pdf_from_file_path(self, file_path: str) -> str:
        try:
            pdf_content = pdfkit.from_file(file_path, False)
        except Exception as e:
            raise ValueError(f"Failed to generate PDF from file: {e}.")

        return pdf_content

    def _save_pdf(self, pdf_content: str, task_id: int) -> str:
        pdf_file_name = f"generated_pdfs/{task_id}.pdf"
        pdf_path = default_storage.save(pdf_file_name, ContentFile(pdf_content))
        return pdf_path


task_services: TaskServices = TaskServices()
