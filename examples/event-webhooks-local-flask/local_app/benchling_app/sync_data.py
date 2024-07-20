

from benchling_api_client.webhooks.v0.beta.models.v2_entity_registered_event import (
    V2EntityRegisteredEvent as V2EntityRegisteredEventBeta,
)
from benchling_sdk.apps.framework import App
from benchling_sdk.apps.status.helpers import ref
from benchling_sdk.models import (
    AppSessionMessageCreate,
    AppSessionMessageStyle,
    AppSessionUpdateStatus,
    CustomEntity,
)

from local_app.lib.postgresql import write_data


def sync_event_data(app: App, entity_registered: V2EntityRegisteredEventBeta) -> None:
    with app.create_session_context(
            name=f"Sync entity {entity_registered.resource_id}", timeout_seconds=30,
        ) as session:
        # Events contain pointers to data, so fetch the full entity data from the API
        entity = app.benchling.custom_entities.get_by_id(entity_registered.resource_id)
        synced_id = _sync_entity(app, entity)
        session.close_session(
            status=AppSessionUpdateStatus.SUCCEEDED,
            messages=[
                AppSessionMessageCreate(
                    f"Synced {ref(entity)} into external database with ID {synced_id}",
                    style=AppSessionMessageStyle.SUCCESS,
                ),
            ],
        )


def _sync_entity(app: App, entity: CustomEntity) -> str:
    field_name = app.config_store.config_by_path(
        ["Synced Schema", "Synced Field Data"],
    ).required().linked_resource().name
    field_value = entity.fields[field_name].value
    field_value = str(field_value) if field_value else None
    return write_data(entity.name, entity.id, field_value)