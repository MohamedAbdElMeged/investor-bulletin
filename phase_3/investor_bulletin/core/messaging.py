
# Create a connection object to publish events
import os
import json
from dotenv import load_dotenv
from amqpstorm import Connection




load_dotenv()
rabbitmq_host = os.environ["RABBITMQ_HOST"]
rabbitmq_user = os.environ["RABBITMQ_USER"]
rabbitmq_password = os.environ["RABBITMQ_PASS"]
exchange_name = "alerts"
queue_name = "alerts_queue"
routing_key = exchange_name + "." + queue_name
broker = Connection(rabbitmq_host,rabbitmq_user,rabbitmq_password)

channel = broker.channel()
# use topic to declacre topic exchange
channel.exchange.declare(exchange_name, "topic",durable=True,auto_delete=False)
#declare the queue
channel.queue.declare(queue_name,durable=True,auto_delete=False)
channel.queue.bind(queue_name, exchange_name, routing_key=routing_key)



def publish_message(body: hash):
    message_str = str(body)

    channel.basic.publish(
                body=json.dumps(body), exchange=exchange_name, routing_key=routing_key
    )

    print(f"Message published: {message_str} with routing_key: {routing_key}")

# if __name__ == "__main__":
    # broker.publish()
