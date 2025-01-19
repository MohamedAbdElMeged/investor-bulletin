# PHASE TWO (Creating publisher/Subscriber)
## Technology used

- Publisher - amqpstorm
- Subscriber - Pika
- Broker RabbitMQ


## Objectives

to be able to publish `THRESHOLD_ALERT` event through a message queue and consume it thought a subscriber to that queue and print the result of that event and create a new alert record

## Functionality

- **Publish a `THRESHOLD_ALERT` event**
- **Consume the `THRESHOLD_ALERT` event and print the message aka the alert**

### How To Run
After run `make up` 
