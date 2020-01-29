from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from venafi.properties.response_objects.config import Config
    from venafi.properties.response_objects.certificate import Certificate
    from venafi.properties.response_objects.log import Log
    from venafi.properties.response_objects.identity import Identity
    from venafi.properties.response_objects.credential import Credential
    from venafi.properties.response_objects.client import Client
    from venafi.properties.response_objects.permissions import Permissions
    from venafi.properties.response_objects.metadata import Metadata
    from venafi.properties.response_objects.rights import Rights
    from venafi.properties.response_objects.secret_store import SecretStore
    from venafi.properties.response_objects.ssh import SSH
    from venafi.properties.response_objects.worfklow import Workflow
    from venafi.properties.response_objects.processing_engines import ProcessingEngines
    from venafi.properties.response_objects.system_status import SystemStatus

    from venafi.features.workflow import RC as ReasonCode
