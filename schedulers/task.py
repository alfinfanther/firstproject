from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery import shared_task
# from bs4 import BeautifulSoup
# from datetime import datetime

logger = get_task_logger(__name__)

@shared_task
def send_email():    
    logger.info("email berhasil di kirim")