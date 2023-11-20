import logging

from celery.exceptions import MaxRetriesExceededError
from config.settings.celery import app
from src.common.enums import ContentType

from ..services import task_services

logger = logging.getLogger(__name__)


@app.task(
    queue="to_pdf",
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_jitter=True,
    max_retries=5,
)
def process_to_pdf(task_id: int, content_type: ContentType, to_pdf: str) -> None:
    try:
        task_services.process_html_to_pdf(task_id, content_type, to_pdf)
    except MaxRetriesExceededError as e:
        logger.exception(
            f"Error while trying make pdf from source '{content_type}', for task '{task_id}'. Error: {e}"
        )
