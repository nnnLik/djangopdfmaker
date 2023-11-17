from django.test import TestCase
from rest_framework import status
from src.core.models import GeneratedPDF, Task


class TaskDetailsViewTestCase(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(status=Task.TaskStatus.IN_PROGRESS)

        generated_pdf = GeneratedPDF.objects.create(pdf_file="some_file.pdf")
        self.task2 = Task.objects.create(
            status=Task.TaskStatus.COMPLETED, generated_pdf=generated_pdf
        )

        self.task3 = Task.objects.create(status=Task.TaskStatus.ERROR)

    def test_get_task_in_progress(self):
        response = self.client.get(f"/api/core/tasks/{self.task1.id}", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], Task.TaskStatus.IN_PROGRESS)
        self.assertEqual(response.data["generated_pdf"], {"pdf_file": None})

    def test_get_task_completed(self):
        response = self.client.get(f"/api/core/tasks/{self.task2.id}", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], Task.TaskStatus.COMPLETED)
        self.assertEqual(response.data["generated_pdf"]["id"], 1)
        self.assertEqual(
            response.data["generated_pdf"]["pdf_file"], "/media/some_file.pdf"
        )

    def test_get_task_error(self):
        response = self.client.get(f"/api/core/tasks/{self.task3.id}", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], Task.TaskStatus.ERROR)
