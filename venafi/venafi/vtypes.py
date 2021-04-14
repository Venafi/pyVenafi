from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from venafi.properties.response_objects.config import Config as _Config
    from venafi.properties.response_objects.certificate import Certificate as _Certificate
    from venafi.properties.response_objects.log import Log as _Log
    from venafi.properties.response_objects.identity import Identity as _Identity
    from venafi.properties.response_objects.credential import Credential as _Credential
    from venafi.properties.response_objects.client import Client as _Client
    from venafi.properties.response_objects.permissions import Permissions as _Permissions
    from venafi.properties.response_objects.metadata import Metadata as _CustomFields
    from venafi.properties.response_objects.rights import Rights as _Rights
    from venafi.properties.response_objects.secret_store import SecretStore as _SecretStore
    from venafi.properties.response_objects.ssh import SSH as _SSH
    from venafi.properties.response_objects.worfklow import Workflow as _Workflow
    from venafi.properties.response_objects.processing_engines import ProcessingEngines as _ProcessingEngines
    from venafi.properties.response_objects.system_status import SystemStatus as _SystemStatus
    from venafi.features.workflow import RC as _ReasonCode

Config = None # type: Optional[_Config]
Certificate = None # type: Optional[_Certificate]
Log = None # type: Optional[_Log]
Identity = None # type: Optional[_Identity]
Credential = None # type: Optional[_Credential]
Client = None # type: Optional[_Client]
Permissions = None # type: Optional[_Permissions]
CustomFields = None # type: Optional[_CustomFields]
Rights = None # type: Optional[_Rights]
SecretStore = None # type: Optional[_SecretStore]
SSH = None # type: Optional[_SSH]
Workflow = None # type: Optional[_Workflow]
ProcessingEngines = None # type: Optional[_ProcessingEngines]
SystemStatus = None # type: Optional[_SystemStatus]
ReasonCode = None # type: Optional[_ReasonCode]
