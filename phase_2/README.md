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
> Prerequiste : please create alert_rule for AAPL symbol beecause it's added for testing with price less than or equal 30.454546
> If you want to create another alert_rule for another symbol please update the `message` object in `/investor_bulletin/core/messaging.py`


After run `make up` 
- run `docker ps`
  the output should be like this
  <img width="863" alt="image" src="https://github.com/user-attachments/assets/51bb7b7b-5b67-48d8-98b0-d3027a8f7bc8" />
  
  take `CONTAINER ID` for `phase_2-web` which will be (in screenshot) `4644cb14931e`

  **For Publishing** 📌
- run `docker exec -it 4644cb14931e /bin/bash` to access backend container
- run these commands
  ```
  cd investor_bulletin/
   python3 -m core.messaging
  ```
  The output should be like this
  ```
  Message published: {'event': 'THRESHOLD_ALERT', 'symbol': 'AAPL', 'price': 30.454546} with routing_key: alerts.alerts_queue
  ```
  **For Consuming** 🎯
  
  - run `docker exec -it 4644cb14931e /bin/bash` to access backend container
  - run these commands
  ```
  cd investor_bulletin/
   python3 -m event_subscriber.main
  ```
  The output should be like this
  ```
  Starting Consuming Service 
  new alert created for AAPL at 2025-01-19 21:41:41.011011 because price reached 30.454546
  ```
  **Test Consuming Thrugh Api**
  - navigate to http://localhost:8000/docs
  - Run `/alert_rules/alerts` endpoint
  <img width="1467" alt="image" src="https://github.com/user-attachments/assets/ff820cba-c285-4aa5-ad12-04791a0b9492" />
