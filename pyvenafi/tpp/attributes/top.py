from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute


class TopAttributes(metaclass=IterableMeta):
    __config_class__ = "Top"
    contact = Attribute('Contact')
    created_by = Attribute('Created By', min_version='15.1')
    description = Attribute('Description')
    disabled = Attribute('Disabled')
    escalation_contact = Attribute('Escalation Contact')
    guid = Attribute('GUID')
    managed_by = Attribute('Managed By')
    metadata = Attribute('Metadata')
    recycle_automatic = Attribute('Recycle Automatic', min_version='22.2')
    recycle_deleted_by = Attribute('Recycle Deleted By', min_version='22.2')
    recycle_deleted_on = Attribute('Recycle Deleted On', min_version='22.2')
    recycle_origin_cn = Attribute('Recycle Origin CN', min_version='22.2')
    recycle_origin_dn = Attribute('Recycle Origin DN', min_version='22.2')
    recycle_origin_parent_cn = Attribute('Recycle Origin Parent CN', min_version='22.2')
    recycle_origin_parent_id = Attribute('Recycle Origin Parent ID', min_version='22.2')
    recycle_origin_parent_pdn = Attribute('Recycle Origin Parent PDN', min_version='22.2')
    reference = Attribute('Reference')
    workflow = Attribute('Workflow')
    workflow_block = Attribute('Workflow Block')
