from datetime import datetime
from typing import List
from properties.response_objects.dataclasses import ssh_certificates
from pytpp.api.api_base import WebSdkEndpoint, WebSdkResponse, ResponseFactory, ResponseField


class _SSHCertificates:
    def __init__(self, api_obj):
        self.CAKeyPair = self._CAKeyPair(api_obj=api_obj)
        self.Request = self._Request(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Template = self._Template(api_obj=api_obj)

    class _CAKeyPair:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)

        class _Create(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='SSHCertificates/CAKeyPair/Create')

            def post(self, name: str, parent_dn: str = None, key_algorithm: str = None,
                     key_storage: str = None, private_key_data: str = None,
                     private_key_passphrase: str = None):
                body = {
                    'Name'                : name,
                    'ParentDN'            : parent_dn,
                    'KeyAlgorithm'        : key_algorithm,
                    'KeyStorage'          : key_storage,
                    'PrivateKeyData'      : private_key_data,
                    'PrivateKeyPassphrase': private_key_passphrase
                }

                class Response(WebSdkResponse):
                    created_on: datetime = ResponseField(alias='CreatedOn')
                    dn: str = ResponseField(alias='DN')
                    fingerprint_sha_256: str = ResponseField(alias='FingerprintSHA256')
                    guid: str = ResponseField(alias='Guid')
                    key_algorithm: str = ResponseField(alias='KeyAlgorithm')
                    key_storage: str = ResponseField(alias='KeyStorage')
                    name: str = ResponseField(alias='Name')
                    processing_details: ssh_certificates.ProcessingDetails = ResponseField(alias='ProcessingDetails')
                    public_key_data: str = ResponseField(alias='PublicKeyData')
                    response: ssh_certificates.Response = ResponseField(alias='Response')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Request(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Request')

        def post(self, ca_dn: str, key_id: str, destination_address: str = None, extensions: str = None, force_command: str = None,
                 object_name: str = None, origin: str = None, policy_dn: str = None, principals: List[str] = None,
                 public_key_data: str = None, source_addresses: List[str] = None, validity_period: str = None,
                 include_certificate_details: bool = False, include_private_key_data: bool = False,
                 private_key_passphrase: str = None, processing_timeout: int = None):
            body = {
                'CADN'                     : ca_dn,
                'KeyId'                    : key_id,
                'DestinationAddress'       : destination_address,
                'Extensions'               : extensions,
                'ForceCommand'             : force_command,
                'ObjectName'               : object_name,
                'Origin'                   : origin,
                'PolicyDN'                 : policy_dn,
                'Principals'               : principals,
                'PublicKeyData'            : public_key_data,
                'SourceAddresses'          : source_addresses,
                'ValidityPeriod'           : validity_period,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData'    : include_private_key_data,
                'PrivateKeyPassphrase'     : private_key_passphrase,
                'ProcessingTimeout'        : processing_timeout
            }

            class Response(WebSdkResponse):
                dn: str = ResponseField(alias='Dn')
                guid: str = ResponseField(alias='Guid')
                processing_details: ssh_certificates.ProcessingDetails = ResponseField(alias='ProcessingDetails')
                response: ssh_certificates.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Retrieve')

        def post(self, dn: str = None, guid: str = None, include_certificate_details: bool = None,
                 include_private_key_data: bool = None, private_key_passphrase: str = None):
            body = {
                'DN'                       : dn,
                'Guid'                     : guid,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData'    : include_private_key_data,
                'PrivateKeyPassphrase'     : private_key_passphrase
            }

            class Response(WebSdkResponse):
                ca_dn: str = ResponseField(alias='CADN')
                ca_guid: str = ResponseField(alias='CAGuid')
                certificate_data: str = ResponseField(alias='CertificateData')
                certificate_details: ssh_certificates.CertificateDetails = ResponseField(alias='CertificateDetails')
                dn: str = ResponseField(alias='DN')
                guid: str = ResponseField(alias='Guid')
                key_id: str = ResponseField(alias='KeyID')
                private_key_data: str = ResponseField(alias='PrivateKeyData')
                processing_details: ssh_certificates.ProcessingDetails = ResponseField(alias='ProcessingDetails')
                public_key_data: str = ResponseField(alias='PublicKeyData')
                request_details: ssh_certificates.RequestDetails = ResponseField(alias='RequestDetails')
                response: ssh_certificates.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Template(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Template')
            self.Retrieve = self._Retrieve(api_obj=api_obj)

        class _Retrieve(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSHCertificates/Template/Retrieve')
                self.PublicKeyData = self._PublicKeyData(api_obj=api_obj)

            def post(self, template_dn: str = None, template_guid: str = None, include_ca_keypair_details: bool = None):
                body = {
                    'DN'                     : template_dn,
                    'Guid'                   : template_guid,
                    'IncludeCAKeyPairDetails': include_ca_keypair_details
                }

                class Response(WebSdkResponse):
                    access_control: ssh_certificates.AccessControl = ResponseField(alias='AccessControl')
                    api_client: ssh_certificates.APIClient = ResponseField(alias='APIClient')
                    ca_keypair_guid: str = ResponseField(alias='CAKeyPairGuid')
                    ca_keypair_dn: str = ResponseField(alias='CAKeyPairDN')
                    ca_keypair: ssh_certificates.CAKeyPair = ResponseField(alias='CAKeyPair')
                    certificate: ssh_certificates.Certificate = ResponseField(alias='Certificate')
                    contacts: List[str] = ResponseField(default_factory=list, alias='Contacts')
                    created_on: datetime = ResponseField(alias='CreatedOn')
                    dn: str = ResponseField(alias='DN')
                    guid: str = ResponseField(alias='Guid')
                    name: str = ResponseField(alias='Name')
                    response: ssh_certificates.Response = ResponseField(alias='Response')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

            class _PublicKeyData(WebSdkEndpoint):
                def __init__(self, api_obj):
                    super().__init__(api_obj=api_obj, url='SSHCertificates/Template/Retrieve/PublicKeyData')

                def get(self, template_dn: str = None, template_guid: str = None):
                    params = {
                        'DN'  : template_dn,
                        'Guid': template_guid,
                    }

                    class Response(WebSdkResponse):
                        response: ssh_certificates.Response = ResponseField(alias='Response')

                    return ResponseFactory(response_cls=Response, response=self._get(params=params))
