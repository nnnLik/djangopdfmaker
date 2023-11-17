import os
from unittest import mock

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from src.common.enums import ContentType
from src.core.models import Task
from src.core.services import task_services, view_services


class TaskServicesTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.media_root = os.path.abspath(settings.MEDIA_ROOT)

    def test_generate_pdf_from_url(self):
        url = "https://en.wikipedia.org/wiki/Metal_Gear_Rising:_Revengeance"
        pdf_content = task_services._generate_pdf_from_url(url)
        self.assertIsNotNone(pdf_content)

    def test_generate_pdf_from_url_incorrect(self):
        url = "http://localhost:5555/"

        with self.assertRaises(ValueError):
            task_services._generate_pdf_from_url(url)

    def test_generate_pdf_from_file_path(self):
        file_path = "tests/core/fixtures/fixt_1.html"
        pdf_content = task_services._generate_pdf_from_file_path(file_path)
        self.assertIsNotNone(pdf_content)

    def test_generate_pdf_from_file_path_incorrect(self):
        file_path = "tests/core/fixtures/fixt_2.pdf"

        with self.assertRaises(ValueError):
            task_services._generate_pdf_from_file_path(file_path)

    def test_save_pdf(self):
        pdf_path = "tests/core/fixtures/fixt_2.pdf"
        task_id = 1

        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        pdf_path_result = task_services._save_pdf(pdf_bytes, task_id)
        self.assertTrue(pdf_path_result.startswith("generated_pdfs/"))
        self._remove_files(f"{self.media_root}/{pdf_path_result}")

    def _remove_files(self, path: str) -> None:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


class ViewServicesTestCase(TestCase):
    @mock.patch("src.core.tasks.process_to_pdf.delay")
    def test_generate_pdf_from_source(self, mock_delay):
        content_type = ContentType.FILE

        pdf_path = "tests/core/fixtures/fixt_1.html"
        file_content = self._get_bytes_from_source(pdf_path)

        uploaded_file = SimpleUploadedFile("some_ultra_data.html", file_content)
        task_id, msg = view_services.generate_pdf_from_source(
            uploaded_file, content_type
        )

        task_obj = Task.objects.get(id=task_id)

        mock_delay.assert_called_once_with(
            task_id, content_type, task_obj.html_source_file.path
        )

        self.assertIsNotNone(task_id)
        self.assertEqual(msg, "Processing started.")

        self._remove_files(task_obj.html_source_file.path)

    def _get_bytes_from_source(self, file_path: str) -> bytes:
        with open(file_path, "rb") as pdf_file:
            return pdf_file.read()

    def _remove_files(self, path: str) -> None:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
