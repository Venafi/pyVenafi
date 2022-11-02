from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class KeyBaseAttributes(MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Key Base"
    algorithm = Attribute('Algorithm')
    approver = Attribute('Approver')
    consumers = Attribute('Consumers')
    disable_automatic_renewal = Attribute('Disable Automatic Renewal')
    in_error = Attribute('In Error')
    internet_email_address = Attribute('Internet EMail Address')
    key_storage_location = Attribute('Key Storage Location')
    label = Attribute('Label')
    last_evaluated_on = Attribute('Last Evaluated On')
    last_notification = Attribute('Last Notification')
    last_renewed_by = Attribute('Last Renewed By')
    last_renewed_on = Attribute('Last Renewed On')
    management_type = Attribute('Management Type')
    max_uses = Attribute('Max Uses')
    origin = Attribute('Origin')
    private_key_vault_id = Attribute('Private Key Vault Id')
    real_name = Attribute('Real Name')
    status = Attribute('Status')
    use_count = Attribute('Use Count')
    validity_period = Attribute('Validity Period')
