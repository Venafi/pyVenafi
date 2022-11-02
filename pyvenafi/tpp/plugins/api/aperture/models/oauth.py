from __future__ import annotations
from pyvenafi.tpp.api.api_base import ObjectModel, ApiField
from pyvenafi.tpp.api.websdk.enums.oauth import Permissions
from typing import List


class Subsystem(ObjectModel):
    name: str = ApiField(alias='name')
    permissions: Permissions = ApiField(alias='permissions')


class ApplicationScope(ObjectModel):
    hidden_subsystems: List[Subsystem] = ApiField(alias='hiddenSubsystems', default_factory=list)
    subsystems: List[Subsystem] = ApiField(alias='subsystems', default_factory=list)
