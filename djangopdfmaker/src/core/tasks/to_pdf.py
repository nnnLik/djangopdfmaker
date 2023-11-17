from celery import shared_task

from ..services import task_services


@shared_task
def process_to_pdf(task_id: int, content_type: str, to_pdf: str) -> None:
    task_services.process_html_to_pdf(task_id, content_type, to_pdf)
