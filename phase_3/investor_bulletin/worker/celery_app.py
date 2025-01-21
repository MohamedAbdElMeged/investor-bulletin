import os
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
load_dotenv()
rabbitmq_host = os.environ["RABBITMQ_HOST"]
rabbitmq_user = os.environ["RABBITMQ_USER"]
rabbitmq_password = os.environ["RABBITMQ_PASS"]


CELERY_BROKER_URL = f"amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}:5672//"
def create_celery_app():
  celery_app = Celery('investor_bulletin_project',
             broker=CELERY_BROKER_URL,
             include=['worker.tasks'])
  
  celery_app.conf.beat_schedule = {
      'get-market-prices-and-check-alert-rules-every-five-minutes': {
          'task': 'worker.tasks.get_market_prices_and_check_alert_rules',
          'schedule': crontab(minute='*')
      }
  }
  return celery_app




celery_app = create_celery_app()

