from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class TopAttributes(metaclass=IterableMeta):
    __config_class__ = "Top"
    contact = Attribute('Contact', min_version='21.4')
    created_by = Attribute('Created By', min_version='21.4')
    description = Attribute('Description', min_version='21.4')
    disabled = Attribute('Disabled', min_version='21.4')
    escalation_contact = Attribute('Escalation Contact', min_version='21.4')
    guid = Attribute('GUID', min_version='21.4')
    managed_by = Attribute('Managed By', min_version='21.4')
    metadata = Attribute('Metadata', min_version='21.4')
    recycle_automatic = Attribute('Recycle Automatic', min_version='22.2')
    recycle_deleted_by = Attribute('Recycle Deleted By', min_version='22.2')
    recycle_deleted_on = Attribute('Recycle Deleted On', min_version='22.2')
    recycle_origin_cn = Attribute('Recycle Origin CN', min_version='22.2')
    recycle_origin_dn = Attribute('Recycle Origin DN', min_version='22.2')
    recycle_origin_parent_cn = Attribute('Recycle Origin Parent CN', min_version='22.2')
    recycle_origin_parent_id = Attribute('Recycle Origin Parent ID', min_version='22.2')
    recycle_origin_parent_pdn = Attribute('Recycle Origin Parent PDN', min_version='22.2')
    reference = Attribute('Reference', min_version='21.4')
    workflow = Attribute('Workflow', min_version='21.4')
    workflow_block = Attribute('Workflow Block', min_version='21.4')
