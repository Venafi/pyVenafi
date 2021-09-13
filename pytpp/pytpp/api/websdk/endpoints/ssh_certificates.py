from typing import List
from pytpp.api.api_base import API, APIResponse, json_response_property
from pytpp.properties.response_objects.ssh_certificates import SSHCertificate


class _SSHCertificates:
    def __init__(self, api_obj):
        self.AddAuthorizedKey = self._AddAuthorizedKey(api_obj=api_obj)
        self.AddHostPrivateKey = self._AddHostPrivateKey(api_obj=api_obj)
        self.AddKnownHostKey = self._AddKnownHostKey(api_obj=api_obj)
        self.AddSelfServiceKey = self._AddSelfServiceKey(api_obj=api_obj)
        self.AddSelfServiceAuthorizedKey = self._AddSelfServiceAuthorizedKey(api_obj=api_obj)
        self.AddSelfServicePrivateKey = self._AddSelfServicePrivateKey(api_obj=api_obj)
        self.AddUserPrivateKey = self._AddUserPrivateKey(api_obj=api_obj)
        self.ApproveKeyOperation = self._ApproveKeyOperation(api_obj=api_obj)
        self.CancelKeyOperation = self._CancelKeyOperation(api_obj=api_obj)
        self.CancelRotation = self._CancelRotation(api_obj=api_obj)
        self.ChangePrivateKeyPassphrase = self._ChangePrivateKeyPassphrase(api_obj=api_obj)
        self.ConfirmSelfServiceKeyInstallation = self._ConfirmSelfServiceKeyInstallation(api_obj=api_obj)
        self.DeleteUnmatchedKeyset = self._DeleteUnmatchedKeyset(api_obj=api_obj)
        self.Devices = self._Devices(api_obj=api_obj)
        self.EditKeyOptions = self._EditKeyOptions(api_obj=api_obj)
        self.EditSelfServiceAuthorizedKey = self._EditSelfServiceAuthorizedKey(api_obj=api_obj)
        self.ExportSelfServiceKey = self._ExportSelfServiceKey(api_obj=api_obj)
        self.ExportSelfServicePrivateKey = self._ExportSelfServicePrivateKey(api_obj=api_obj)
        self.ImportAuthorizedKey = self._ImportAuthorizedKey(api_obj=api_obj)
        self.ImportKeyUsageData = self._ImportKeyUsageData(api_obj=api_obj)
        self.ImportPrivateKey = self._ImportPrivateKey(api_obj=api_obj)
        self.KeyDetails = self._KeyDetails(api_obj=api_obj)
        self.KeysetDetails = self._KeysetDetails(api_obj=api_obj)
        self.KeyUsage = self._KeyUsage(api_obj=api_obj)
        self.MoveKeysetsToPolicy = self._MoveKeysetsToPolicy(api_obj=api_obj)
        self.RejectKeyOperation = self._RejectKeyOperation(api_obj=api_obj)
        self.RemoveKey = self._RemoveKey(api_obj=api_obj)
        self.RetryKeyOperation = self._RetryKeyOperation(api_obj=api_obj)
        self.RetryRotation = self._RetryRotation(api_obj=api_obj)
        self.Rotate = self._Rotate(api_obj=api_obj)
        self.SetUnmatchedKeysetPassPhrase = self._SetUnmatchedKeysetPassPhrase(api_obj=api_obj)
        self.SkipKeyRotation = self._SkipKeyRotation(api_obj=api_obj)
        self.TestDeviceConnection = self._TestDeviceConnection(api_obj=api_obj)
        self.Widget = self._Widget(api_obj=api_obj)

    class _Request(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Request')

        def post(self, ca_dn: str,
                 key_id: str,
                 destination_address: str = None,
                 extensions: str = None,
                 force_command: str = None,
                 object_name: str = None,
                 origin: str = None,
                 policy_dn: str = None,
                 principals: List[str] = None,
                 public_key_data: str = None,
                 source_addresses: List[str] = None,
                 validity_period: str = None
                 ):

            body = {
                'CADN': ca_dn,
                'KeyId': key_id,
                'DestinationAddress': destination_address,
                'Extensions': extensions,
                'ForceCommand': force_command,
                'ObjectName': object_name,
                'Origin': origin,
                'PolicyDN': policy_dn,
                'Principals': principals,
                'PublicKeyData': public_key_data,
                'SourceAddresses': source_addresses,
                'ValidityPeriod': validity_period
            }
            

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @json_response_property()
                def ssh_certificate_dn(self) -> str:
                    return self._from_json('DN')

                @property
                @json_response_property()
                def ssh_certificate_guid(self) -> str:
                    return self._from_json('Guid')

                @property
                @json_response_property()
                def response(self) -> SSHCertificate.Response:
                    return SSHCertificate.Response(self._from_json('Response'))

                @property
                @json_response_property()
                def processing_details(self) -> SSHCertificate.ProcessingDetails:
                    return SSHCertificate.ProcessingDetails(self._from_json('ProcessingDetails'))


            return _Response(response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Retrieve')

        def post(self, certificate_dn: str = None,
                 certificate_guid: str = None,
                 include_certificate_details: bool = None,
                 include_private_key_data: bool = None,
                 private_key_passphrase: str = None):

            body = {
                'DN': certificate_dn,
                'Guid': certificate_guid,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData': include_private_key_data,
                'PrivateKeyPassphrase': private_key_passphrase
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @json_response_property()
                def ca_dn(self) -> str:
                    return self._from_json('CADN')

                @property
                @json_response_property()
                def ca_guid(self) -> str:
                    return self._from_json('CAGuid')

                @property
                @json_response_property()
                def certificate_data(self) -> str:
                    return self._from_json('CertificateData')

                @property
                @json_response_property()
                def certificate_details(self) -> SSHCertificate.CertificateDetails:
                    return SSHCertificate.CertificateDetails(self._from_json('CertificateDetails'))

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json('Guid')

                @property
                @json_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyID')

                @property
                @json_response_property()
                def private_key_data(self) -> str:
                    return self._from_json('PrivateKeyData')

                @property
                @json_response_property()
                def processing_details(self) -> SSHCertificate.ProcessingDetails:
                    return SSHCertificate.ProcessingDetails(self._from_json('PrivateKeyData'))

                @property
                @json_response_property()
                def public_key_data(self) -> str:
                    return self._from_json('PublicKeyData')

                @property
                @json_response_property()
                def request_details(self) -> SSHCertificate.RequestDetails:
                    return SSHCertificate.RequestDetails(self._from_json('PublicKeyData'))

                @property
                @json_response_property()
                def response(self):
                    return SSHCertificate.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _Template(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Template')

        class _Retrieve(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSHCertificates/Template/Retrieve')

            def post(self, template_dn: str = None, template_guid: str = None, include_ca_keypair_details: bool = None):
                body = {
                    'DN': template_dn,
                    'Guid'  : template_guid,
                    'IncludeCAKeyPairDetails' : include_ca_keypair_details
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @json_response_property()
                    def access_control(self) -> dict:
                        return self._from_json('AccessControl')

                    @property
                    @json_response_property()
                    def api_client(self) -> SSHCertificate.APIClient:
                        return SSHCertificate.APIClient(self._from_json('APIClient'))

                    @property
                    @json_response_property()
                    def ca_keypair_guid(self) -> str:
                        return self._from_json('CAKeyPairGuid')

                    @property
                    @json_response_property()
                    def ca_keypair_dn(self) -> str:
                        return self._from_json('CAKeyPairDN')

                    @property
                    @json_response_property()
                    def ca_keypair(self) -> SSHCertificate.CAKeyPair:
                        return SSHCertificate.CAKeyPair(self._from_json('CAKeyPair'))

                    @property
                    @json_response_property()
                    def certificate(self) -> SSHCertificate.Certificate:
                        return SSHCertificate.Certificate(self._from_json('Certificate'))

                    @property
                    @json_response_property()
                    def contacts(self) -> List[str]:
                        return self._from_json('Contacts')

                    @property
                    @json_response_property()
                    def created_on(self) -> str:
                        return self._from_json('CreatedOn')

                    @property
                    @json_response_property()
                    def guid(self) -> str:
                        return self._from_json('Guid')

                    @property
                    @json_response_property()
                    def name(self) -> str:
                        return self._from_json('Name')

                    @property
                    @json_response_property()
                    def response(self):
                        return SSHCertificate.Response(self._from_json('Response'))

                return _Response(response=self._post(data=body))

            class _PublicKeyData(API):
                def __init__(self, api_obj):
                    super().__init__(api_obj=api_obj, url='SSHCertificates/Template/Retrieve/PublicKeyData')

                def get(self, template_dn: str = None, template_guid: str = None):
                    params = {
                        'DN'  : template_dn,
                        'Guid': template_guid,
                    }

                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        def response(self) -> str:
                            return self.response

                    return _Response(response=self._get(params=params))
