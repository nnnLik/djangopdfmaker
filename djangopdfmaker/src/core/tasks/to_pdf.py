from celery import shared_task

from ..services import task_services


@shared_task
def process_to_pdf(task_id: int, type: str, to_pdf: str) -> None:
    task_services.process_html_to_pdf(task_id, type, to_pdf)
