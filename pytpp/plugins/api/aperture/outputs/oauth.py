from pytpp.api.api_base import OutputModel, ApiField
from pytpp.api.websdk.enums.oauth import Permissions
from typing import List


class ApplicationScope(OutputModel):
    hidden_subsystems: 'List[Subsystem]' = ApiField(alias='hiddenSubsystems')
    subsystems: 'List[Subsystem]' = ApiField(alias='subsystems')


class Subsystem(OutputModel):
    name: str = ApiField(alias='name')
    permissions: Permissions = ApiField(alias='permissions')
