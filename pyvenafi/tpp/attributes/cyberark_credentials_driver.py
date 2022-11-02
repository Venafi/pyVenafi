from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.credential_driver_base import CredentialDriverBaseAttributes


class CyberArkCredentialsDriverAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "CyberArk Credentials Driver"
    ccp_certificate_credential = Attribute('CCP Certificate Credential')
    central_credential_provider_web_service_url = Attribute('Central Credential Provider Web Service URL')
    password_retrieval_method = Attribute('Password Retrieval Method')
    scim_server_url = Attribute('SCIM Server URL')
    scim_server_user = Attribute('SCIM Server User')
    use_proxy = Attribute('Use Proxy')
    web_service_url = Attribute('Web Service URL')
    web_service_user = Attribute('Web Service User')
    web_services_authentication_method = Attribute('Web Services Authentication Method')
    windows_credential_provider_version = Attribute('Windows Credential Provider Version')
