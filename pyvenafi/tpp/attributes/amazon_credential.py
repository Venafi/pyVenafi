from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes


class AmazonCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Amazon Credential"
    authentication_credential = Attribute('Authentication Credential')
    authentication_source = Attribute('Authentication Source')
    ec2_assigned_role = Attribute('EC2 Assigned Role')
    region_code = Attribute('Region Code')
    role = Attribute('Role')
    web_service_url = Attribute('Web Service URL')
