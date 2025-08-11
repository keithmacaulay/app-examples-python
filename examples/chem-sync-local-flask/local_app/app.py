import asyncio
import json
import os
from typing import Any

from benchling_sdk.apps.helpers.webhook_helpers import verify
from faststream.rabbit import RabbitBroker
from flask import Flask, request

from local_app.benchling_app.setup import app_definition_id
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

# Initialize FastStream broker for publishing
broker = RabbitBroker(url=connection_url)


def create_app() -> Flask:
    app = Flask("benchling-app")

    @app.route("/health")
    def health_check() -> tuple[str, int]:
        # Just a route allowing us to check that Flask itself is up and running
        return "OK", 200

    @app.route("/1/webhooks/<path:target>", methods=["POST"])
    def receive_webhooks(target: str) -> tuple[str, int]:  # noqa: ARG001
        # For security, don't do anything else without first verifying the webhook
        app_def_id = app_definition_id()

        # Important! To verify webhooks, we need to pass the body as an unmodified string
        # Flask's request.data is bytes, so decode to string. Passing bytes or JSON won't work
        verify(app_def_id, request.data.decode("utf-8"), request.headers)

        logger.debug("Received webhook message: %s", request.json)
        # Dispatch work and ACK webhook as quickly as possible
        _enqueue_work()
        # ACK webhook by returning 2xx status code so Benchling knows the app received the signal
        return "OK", 200

    return app


def _enqueue_work() -> None:
    """Publish webhook message to RabbitMQ broker for asynchronous processing."""
    try:
        message = json.dumps(request.json)
        
        # Run the async publish operation
        asyncio.run(_publish_message_async(message))
        
        logger.debug("Successfully published webhook message to RabbitMQ queue: %s", RABBITMQ_QUEUE)
            
    except Exception as e:
        logger.error("Error publishing to RabbitMQ: %s", e)

async def _publish_message_async(message: str) -> None:
    """Async function to publish message using FastStream broker."""
    async with broker:
        await broker.publish(
            message,
            queue=RABBITMQ_QUEUE,
            persist=True  # Make message persistent
        )
