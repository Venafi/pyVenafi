from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes

class PlacementJobAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Placement Job"
    archive_old_certificates = Attribute('Archive Old Certificates', min_version='21.4')
    default_container = Attribute('Default Container', min_version='21.4')
    include_subfolders = Attribute('Include Subfolders', min_version='21.4')
    last_run = Attribute('Last Run', min_version='21.4')
    layout_rules = Attribute('Layout Rules', min_version='21.4')
    objects_combined = Attribute('Objects Combined', min_version='21.4')
    objects_evaluated = Attribute('Objects Evaluated', min_version='21.4')
    objects_moved = Attribute('Objects Moved', min_version='21.4')
    progress = Attribute('Progress', min_version='21.4')
    rules_order = Attribute('Rules Order', min_version='21.4')
    scan_folders = Attribute('Scan Folders', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
