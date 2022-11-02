from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes


class GoogleCloudAppAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Google Cloud App"
    file_validation_disabled = Attribute('File Validation Disabled')
    google_project_name = Attribute('Google Project Name')
    network_validation_disabled = Attribute('Network Validation Disabled')
    target_proxy_name = Attribute('Target Proxy Name')
    target_proxy_type = Attribute('Target Proxy Type')
    target_region = Attribute('Target Region')
    target_resource = Attribute('Target Resource')
    timeout = Attribute('Timeout')
