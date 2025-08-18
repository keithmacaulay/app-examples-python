from benchling_sdk.apps.canvas.framework import CanvasBuilder
from benchling_sdk.apps.canvas.types import UiBlock
from benchling_sdk.apps.framework import App
from benchling_sdk.models import (
    ButtonUiBlock,
    ButtonUiBlockType,
    MarkdownUiBlock,
    MarkdownUiBlockType,
)
from benchling_sdk.models.webhooks.v0 import (
    CanvasCreatedWebhookV2,
    CanvasInitializeWebhookV2,
)


def render_search_canvas(app: App, canvas_initialized: CanvasInitializeWebhookV2) -> None:
    with app.create_session_context("Show Canvas Showcase - Start", timeout_seconds=20):
        canvas_builder = CanvasBuilder(
            app_id=app.id,
            feature_id=canvas_initialized.feature_id,
            resource_id=canvas_initialized.resource_id,
        )
        canvas_builder.blocks.append(start_blocks())
        app.benchling.apps.create_canvas(canvas_builder.to_create())


def render_search_canvas_for_created_canvas(app: App, canvas_created: CanvasCreatedWebhookV2) -> None:
    with app.create_session_context("Show Canvas Showcase - Start", timeout_seconds=20):
        canvas_builder = CanvasBuilder(app_id=app.id, feature_id=canvas_created.feature_id)
        canvas_builder.blocks.append(start_blocks())
        app.benchling.apps.update_canvas(canvas_created.canvas_id, canvas_builder.to_update())


def start_blocks() -> list[UiBlock]:
    return [
        MarkdownUiBlock(
            id="intro",
            type=MarkdownUiBlockType.MARKDOWN,
            value="This example app demonstrates the use of App Canvas, and the various UI blocks that can be used to create a canvas. This App can embedded in both the Notebook and via Runs.",
        ),
        MarkdownUiBlock(
            id="intro1",
            type=MarkdownUiBlockType.MARKDOWN,
            value="Each page of the app demonstrates a different UI block, and code examples of how to use it (either via the API or the Benchling SDK).",
        ),
        MarkdownUiBlock(
            id="intro2",
            type=MarkdownUiBlockType.MARKDOWN,
            value="At the end of each page, there is a button to navigate to the next page. You can also navigate back to the previous page using the previous button.",
        ),
        ButtonUiBlock(
            id="next_0",
            text="Next >",
            type=ButtonUiBlockType.BUTTON,
        ),
    ]
