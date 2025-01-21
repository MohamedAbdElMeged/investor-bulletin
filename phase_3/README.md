# PHASE THREE (Background tasks)
## Technology used

* Background task - Celery
* Schedular - celery beat

# Objectives

to be able to fetch the market data periodically every 5 minutes and check if any of any of the stocks crossed those thresholds that was sets by the users in our rules table and fire an event to alert the user based on that

## Functionality

* Background task to fetch market data for symbols mentioned in phase one

* publish event for each symbol synced with the new price

* schedule to trigger the task every 5 minutes

### Instructions:
- created celery beat to run the background task every 5 minutes
- fixing some transaction issues in dal files to make sure that transactions are isolated and running correctly
- add some loggers
- add celery-worker , celery-beat, event-consumer  services in docker compose
  

### How To Run

Just run `make up`, create your desired alert rules and let the magic begins 🪄 🧙‍♂️

### Examples

