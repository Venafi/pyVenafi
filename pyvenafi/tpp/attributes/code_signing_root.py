from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes


class CodeSigningRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Root"
    archive_last_evaluated_on = Attribute('Archive Last Evaluated On', min_version='22.3')
    default_ca_container = Attribute('Default CA Container', min_version='19.2')
    default_certificate_container = Attribute('Default Certificate Container', min_version='19.2')
    default_credential_container = Attribute('Default Credential Container', min_version='19.2')
    disable_jwk_public_key_server = Attribute('Disable JWK Public Key Server', min_version='23.1')
    enforce_group_roles = Attribute('Enforce Group Roles', min_version='19.2')
    environment_template_update_flow_dn = Attribute('Environment Template Update Flow DN', min_version='21.4')
    flow_instance_macro = Attribute('Flow Instance Macro', min_version='19.3')
    key_storage_location = Attribute('Key Storage Location', min_version='19.2')
    key_use_timeout = Attribute('Key Use Timeout', min_version='19.2')
    max_archive_age_days = Attribute('Max Archive Age Days', min_version='22.3')
    max_environment_count = Attribute('Max Environment Count', min_version='23.1')
    prevent_self_dealing = Attribute('Prevent Self Dealing', min_version='19.2')
    prevent_unlimited_signings = Attribute('Prevent Unlimited Signings', min_version='23.1')
    project_delete_flow_dn = Attribute('Project Delete Flow DN', min_version='21.1')
    project_description_tooltip = Attribute('Project Description Tooltip', min_version='19.2')
    request_in_progress_message = Attribute('Request In Progress Message', min_version='19.3')
    storage_driver = Attribute('Storage Driver', min_version='22.3')
