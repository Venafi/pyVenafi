from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class OnboardDiscoveryAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Onboard Discovery"
    amazon_account_ids = Attribute('Amazon Account Ids')
    application_type = Attribute('Application Type')
    azure_application_id = Attribute('Azure Application Id')
    azure_tenant_id = Attribute('Azure Tenant Id')
    certificates_placement_folder = Attribute('Certificates Placement Folder')
    credential = Attribute('Credential')
    default_container = Attribute('Default Container')
    device = Attribute('Device')
    devices_folder = Attribute('Devices Folder')
    disable_installations_not_in_use = Attribute('Disable Installations Not In Use')
    driver_name = Attribute('Driver Name')
    environment = Attribute('Environment')
    extract_private_key = Attribute('Extract Private Key')
    in_progress = Attribute('In Progress')
    last_run = Attribute('Last Run')
    last_update = Attribute('Last Update')
    log_debug = Attribute('Log Debug')
    onboard_discovery_import_work_to_do = Attribute('Onboard Discovery Import Work To Do')
    port = Attribute('Port')
    profiles_to_import = Attribute('Profiles To Import')
    result_count = Attribute('Result Count')
    script_execution_timeout = Attribute('Script Execution Timeout')
    script_hash_mismatch_error = Attribute('Script Hash Mismatch Error')
    status = Attribute('Status')
    stop_requested = Attribute('Stop Requested')
    timeout = Attribute('Timeout')
    xml_port = Attribute('XML Port')
