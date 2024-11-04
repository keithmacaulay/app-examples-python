from threading import Thread

from benchling_sdk.apps.helpers.webhook_helpers import verify
from flask import Flask, request

from local_app.benchling_app.handler import handle_webhook
from local_app.benchling_app.setup import app_definition_id
from local_app.lib.logger import get_logger

logger = get_logger()


def create_app() -> Flask:
    app = Flask("benchling-app")

    @app.route("/health")
    def health_check() -> tuple[str, int]:
        # Just a route allowing us to check that Flask itself is up and running
        return "OK", 200

    @app.route("/<path:target>", methods=["POST"])
    def receive_webhooks(target: str) -> tuple[str, int]:  # noqa: ARG001
        # TODO: Verify webhook from Benchling and dispatch the work
        # For security, don't do anything else without first verifying the webhook
        # app_def_id = app_definition_id()
        # verify(app_def_id, request.data.decode("utf-8"), request.headers) # type: ignore[arg-type]

        logger.debug("Received webhook message: %s", request.json)
        # Dispatch work and ACK webhook as quickly as possible
        # _enqueue_work()
        # ACK webhook by returning 2xx status code so Benchling knows the app received the signal
        return "OK", 200

    return app


def _enqueue_work() -> None:
    # PRODUCTION NOTE: A high volume of webhooks may spawn too many threads and lead to processing failures
    # In production, we recommend a more robust queueing system for scale
    thread = Thread(
        target=handle_webhook,
        args=(request.json,),
    )
    thread.start()
