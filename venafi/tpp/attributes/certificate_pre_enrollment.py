from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class CertificatePreEnrollmentAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Pre-Enrollment"
