from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class WorkflowTicketAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Workflow Ticket"
    approval_explanation = Attribute('Approval Explanation', min_version='21.4')
    approval_from = Attribute('Approval From', min_version='21.4')
    approval_reason = Attribute('Approval Reason', min_version='21.4')
    approver_not_found_timestamp = Attribute('Approver Not Found Timestamp', min_version='21.4')
    creation_date = Attribute('Creation Date', min_version='21.4')
    last_notification = Attribute('Last Notification', min_version='21.4')
    last_update = Attribute('Last Update', min_version='21.4')
    notified_on = Attribute('Notified On', min_version='24.1')
    owner_object = Attribute('Owner Object', min_version='21.4')
    scheduled_start = Attribute('Scheduled Start', min_version='21.4')
    scheduled_stop = Attribute('Scheduled Stop', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
    suspended_attribute = Attribute('Suspended Attribute', min_version='21.4')
    updated_by = Attribute('Updated By', min_version='21.4')
    user_data = Attribute('User Data', min_version='21.4')
    workflow = Attribute('Workflow', min_version='21.4')
