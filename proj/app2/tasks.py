from proj.celery import app
from celery.utils.log import get_task_logger
from .email import send_review_email_task

logger = get_task_logger(__name__)

@app.task(name='send_review_email_task')
def send_review_email_task(name, email, review):
    logger.info('Send review email')
    return send_review_email_task(name, email, review)