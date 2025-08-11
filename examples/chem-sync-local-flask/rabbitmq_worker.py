#!/usr/bin/env python3
"""
RabbitMQ Worker Service using FastStream

This script subscribes to the RabbitMQ queue and processes webhook messages
by calling the handle_webhook function using FastStream.
"""

import asyncio
import json
import os
from contextlib import asynccontextmanager

from faststream import FastStream
from faststream.rabbit import (
    RabbitBroker, 
    RabbitExchange, 
    ExchangeType,
    RabbitQueue,
)

from local_app.benchling_app.handler import handle_webhook
from local_app.lib.logger import get_logger

logger = get_logger()

# RabbitMQ configuration
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")
RABBITMQ_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_DEFAULT_PASS")

# Build RabbitMQ connection URL
connection_url = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
exchange = RabbitExchange(name="benchling_webhooks", durable=True, type=ExchangeType.TOPIC)
queue = RabbitQueue(name=RABBITMQ_QUEUE, durable=True)

# Initialize FastStream broker
broker = RabbitBroker(url=connection_url)

@asynccontextmanager
async def lifespan():
    """Application lifespan handler for startup and shutdown."""
    logger.info("Starting FastStream RabbitMQ worker...")
    logger.info("Connecting to RabbitMQ broker at %s:%s", RABBITMQ_HOST, RABBITMQ_PORT)
    yield
    logger.info("Stopping FastStream RabbitMQ worker...")

# Initialize FastStream app
app = FastStream(broker, lifespan=lifespan)

@broker.subscriber(queue, exchange)
async def process_webhook_message(body: str):
    """Process webhook messages from the RabbitMQ queue."""
    try:
        logger.info("📨 Received message from queue %s", RABBITMQ_QUEUE)
        logger.info("📄 Message payload: %s", body)
        
        # Parse the JSON message
        webhook_dict = json.loads(body)
        logger.info("✅ Parsed webhook message successfully")
        
        # Process the webhook
        logger.info("🔄 Processing webhook message...")
        handle_webhook(webhook_dict)
        logger.info("✅ Successfully processed webhook message")
        
    except json.JSONDecodeError as e:
        logger.error("❌ Failed to parse message as JSON: %s", e)
        raise  # Let FastStream handle the error and decide on requeue/reject
    except Exception as e:
        logger.error("❌ Error processing webhook message: %s", e)
        raise  # Let FastStream handle the error and decide on requeue/reject

if __name__ == "__main__":
    logger.info("FastStream RabbitMQ worker is running. Press Ctrl+C to stop.")
    logger.info("Waiting for messages from queue '%s'", RABBITMQ_QUEUE)
    asyncio.run(app.run())
