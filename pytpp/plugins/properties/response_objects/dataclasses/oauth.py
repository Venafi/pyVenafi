from dataclasses import dataclass
from pytpp.properties.response_objects.dataclasses.oauth import Permissions
from typing import List


@dataclass
class ApplicationScope:
    hidden_subsystems: 'List[OAuth.Subsystem]'
    subsystems: 'List[OAuth.Subsystem]'


@dataclass
class Subsystem:
    name: str
    permissions: Permissions
