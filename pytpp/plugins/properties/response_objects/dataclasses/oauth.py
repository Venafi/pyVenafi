from dataclasses import dataclass
from pytpp.properties.oauth import Permissions
from typing import List


@dataclass
class ApplicationScope:
    hidden_subsystems: 'List[Subsystem]'
    subsystems: 'List[Subsystem]'


@dataclass
class Subsystem:
    name: str
    permissions: Permissions
