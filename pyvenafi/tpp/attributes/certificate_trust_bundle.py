from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.device import DeviceAttributes


class CertificateTrustBundleAttributes(DeviceAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Trust Bundle"
    excluded_certificates = Attribute('Excluded Certificates')
    included_certificates = Attribute('Included Certificates')
    is_match = Attribute('Is Match')
