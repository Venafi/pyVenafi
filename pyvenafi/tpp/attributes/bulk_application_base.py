from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes


class BulkApplicationBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Bulk Application Base"
    batch_size = Attribute('Batch Size')
    certificate_thumbprint = Attribute('Certificate Thumbprint')
    device = Attribute('Device')
    exclude_expired_certificates = Attribute('Exclude Expired Certificates')
    exclude_historical_certificates = Attribute('Exclude Historical Certificates')
    exclude_revoked_certificates = Attribute('Exclude Revoked Certificates')
    grouping_id = Attribute('Grouping Id')
    in_error = Attribute('In Error')
    in_progress = Attribute('In Progress')
    last_run = Attribute('Last Run')
    last_update = Attribute('Last Update')
    light_run = Attribute('Light Run')
    light_run_new_certificates_threshold = Attribute('Light Run New Certificates Threshold')
    maximum_days_expired = Attribute('Maximum Days Expired')
    policydn = Attribute('PolicyDN')
    status = Attribute('Status')
    stop_requested = Attribute('Stop Requested')
