from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningProjectAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Project"
    approval_submission_date = Attribute('Approval Submission Date')
    auditor = Attribute('Auditor')
    certificate_issue_flow_dn = Attribute('Certificate Issue Flow DN')
    certificate_owner = Attribute('Certificate Owner')
    code_signing_application_dn = Attribute('Code Signing Application DN')
    flow_instance_macro = Attribute('Flow Instance Macro')
    key_issue_flow_dn = Attribute('Key Issue Flow DN')
    key_owner = Attribute('Key Owner')
    key_use_approver = Attribute('Key Use Approver')
    key_user = Attribute('Key User')
    owner = Attribute('Owner')
    project_delete_flow_dn = Attribute('Project Delete Flow DN')
    purpose = Attribute('Purpose')
    risk_level = Attribute('Risk Level')
    status = Attribute('Status')
