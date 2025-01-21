
import pika
import json
import os
from datetime import datetime
from pika.exchange_type import ExchangeType
from dotenv import load_dotenv
from resources.alerts.alert_service import create_new_alert
from resources.alerts.alert_schema import AlertCreate
from resources.alert_rules.alert_rule_service import get_all_alert_rules_by_symbol
from db.models.models import session, SessionLocal
load_dotenv()

def init_subscriber():
      credentials = pika.PlainCredentials(os.environ["RABBITMQ_USER"], os.environ["RABBITMQ_PASS"])
      connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["RABBITMQ_HOST"], credentials=credentials))
      return connection

def process_threshold_alert_body(body):
    print("new event process")
    symbol = body["symbol"]
    price = float(body["price"])
    alert_rules = get_all_alert_rules_by_symbol(symbol,SessionLocal)
    for alert_rule in alert_rules:
        if price >= alert_rule.threshold_price and symbol == alert_rule.symbol:
            print("new alert")
            alert_create = AlertCreate(symbol=symbol,stock_price=price,alert_rule_id=alert_rule.id,triggered_at=datetime.now())
            new_alert = create_new_alert(alert_create,SessionLocal)
            print(f"new alert created for {new_alert.symbol} at {new_alert.triggered_at} because price reached {new_alert.stock_price}")

    return
def on_event(ch, method, properties, body):
    print("new event come")
    if body is not  None:
        body = json.loads(body)
        if body["event"] == "THRESHOLD_ALERT":
            process_threshold_alert_body(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    print("Starting Consuming Service ")
    print(os.environ["RABBITMQ_USER"])
    connection = init_subscriber()
    channel = connection.channel()
    queue_name = "alerts_queue"
    exchange_name = "alerts"
    routing_key = exchange_name + "." + queue_name
    channel.exchange_declare(
        exchange= exchange_name,
        exchange_type= ExchangeType.topic,durable=True,auto_delete=False)
    
    channel.queue_declare(queue=queue_name,durable=True, auto_delete=False)
    channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)
    channel.basic_consume(queue=queue_name, on_message_callback=on_event)
    channel.start_consuming()


  


