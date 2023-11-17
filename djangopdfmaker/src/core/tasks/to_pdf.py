from celery import shared_task
from src.common.enums import ContentType

from ..services import task_services


@shared_task
def process_to_pdf(task_id: int, content_type: ContentType, to_pdf: str) -> None:
    task_services.process_html_to_pdf(task_id, content_type, to_pdf)
