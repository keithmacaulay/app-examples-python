from benchling_sdk.apps.canvas.framework import CanvasBuilder, AppCanvasUpdate
from benchling_sdk.apps.framework import App
from benchling_sdk.apps.status.errors import AppUserFacingError
from benchling_sdk.models.webhooks.v0 import CanvasInteractionWebhookV2

from local_app.benchling_app.blocks import blocks
from local_app.benchling_app.views.canvas_initialize import start_blocks
from local_app.lib.logger import get_logger

logger = get_logger()


class UnsupportedButtonError(Exception):
    pass

def route_interaction_webhook(app: App, canvas_interaction: CanvasInteractionWebhookV2) -> None:
    canvas_id = canvas_interaction.canvas_id
    if canvas_interaction.button_id:
        button_type, button_id=canvas_interaction.button_id.split("_", 1)
        button_id = int(button_id)
        logger.info(f"Button type: {button_type}, Button id: {button_id}")
        # next button has been clicked, render the next block
        if button_type == "next":
            next_block_id = button_id
        # prev button has been clicked, render the previous block
        elif button_type == "prev":
            next_block_id = button_id - 2
        else:
            app.benchling.apps.update_canvas(canvas_interaction.canvas_id, AppCanvasUpdate(enabled=True))
            raise UnsupportedButtonError(
                f"Whoops, the developer forgot to handle the button {canvas_interaction.button_id} with type {button_type} and id {button_id} ",
            )
        with app.create_session_context(f"Render Canvas {next_block_id}", timeout_seconds=20) as session:
            session.attach_canvas(canvas_id)
            canvas_builder = _canvas_builder_from_canvas_id(app, canvas_id)
            if next_block_id < 0:
                this_blocks = start_blocks()
            else:
                this_blocks = blocks[next_block_id]
            canvas_builder = canvas_builder\
                .with_blocks(this_blocks)\
                .with_enabled()
            session.app.benchling.apps.update_canvas(canvas_id, canvas_builder.to_update())

    else:
        # Re-enable the Canvas, or it will stay disabled and the user will be stuck
        app.benchling.apps.update_canvas(canvas_interaction.canvas_id, AppCanvasUpdate(enabled=True))
        # Not shown to user by default, for our own logs cause we forgot to handle some button
        # This is developer error
        raise UnsupportedButtonError(
            f"Whoops, the developer forgot to handle the button {canvas_interaction.button_id}",
        )

def _canvas_builder_from_canvas_id(app: App, canvas_id: str) -> CanvasBuilder:
    current_canvas = app.benchling.apps.get_canvas_by_id(canvas_id)
    return CanvasBuilder.from_canvas(current_canvas)