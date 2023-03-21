from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class JSSDiscoveryAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Discovery"
    cluster = Attribute('Cluster')
    credential = Attribute('Credential')
    default_container = Attribute('Default Container')
    delete_missing_certificates = Attribute('Delete Missing Certificates')
    delete_missing_clusters = Attribute('Delete Missing Clusters')
    description = Attribute('Description')
    discover_inactive_clusters = Attribute('Discover Inactive Clusters')
    ignore_certificates_valid_less_than = Attribute('Ignore Certificates Valid Less Than')
    import_summary = Attribute('Import Summary')
    include_expired_certificates = Attribute('Include Expired Certificates')
    jss_api_base_url = Attribute('JSS API Base URL')
    jss_auth_audience = Attribute('JSS Auth Audience')
    jss_auth_endpoint = Attribute('JSS Auth Endpoint')
    jss_client_id = Attribute('JSS Client ID')
    jss_client_secret = Attribute('JSS Client Secret')
    last_run = Attribute('Last Run')
    missing_certificates_policy_folder = Attribute('Missing Certificates Policy Folder')
    missing_clusters_policy_folder = Attribute('Missing Clusters Policy Folder')
    retire_missing_certificates = Attribute('Retire Missing Certificates')
    revoke_missing_certificates = Attribute('Revoke Missing Certificates')
    revoke_prevention_period = Attribute('Revoke Prevention Period')
    status = Attribute('Status')
    timeout = Attribute('Timeout')
