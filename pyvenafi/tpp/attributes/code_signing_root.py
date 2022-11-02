from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class CodeSigningRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Root"
    archive_last_evaluated_on = Attribute('Archive Last Evaluated On')
    default_ca_container = Attribute('Default CA Container')
    default_certificate_container = Attribute('Default Certificate Container')
    default_credential_container = Attribute('Default Credential Container')
    enforce_group_roles = Attribute('Enforce Group Roles')
    environment_template_update_flow_dn = Attribute('Environment Template Update Flow DN')
    flow_instance_macro = Attribute('Flow Instance Macro')
    key_storage_location = Attribute('Key Storage Location')
    key_use_timeout = Attribute('Key Use Timeout')
    max_archive_age_days = Attribute('Max Archive Age Days')
    prevent_self_dealing = Attribute('Prevent Self Dealing')
    project_delete_flow_dn = Attribute('Project Delete Flow DN')
    project_description_tooltip = Attribute('Project Description Tooltip')
    request_in_progress_message = Attribute('Request In Progress Message')
    storage_driver = Attribute('Storage Driver')
