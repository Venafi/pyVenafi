from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.certificate import Certificate
from venafi.tools.helpers.date_converter import from_date_string


class _Certificates(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Certificates')
        self.Associate = self._Associate(websdk_obj=websdk_obj)
        self.CheckPolicy = self._CheckPolicy(websdk_obj=websdk_obj)
        self.Dissociate = self._Dissociate(websdk_obj=websdk_obj)
        self.Import = self._Import(websdk_obj=websdk_obj)
        self.Push = self._Push(websdk_obj=websdk_obj)
        self.Renew = self._Renew(websdk_obj=websdk_obj)
        self.Request = self._Request(websdk_obj=websdk_obj)
        self.Reset = self._Reset(websdk_obj=websdk_obj)
        self.Retrieve = self._Retrieve(websdk_obj=websdk_obj)
        self.Retry = self._Retry(websdk_obj=websdk_obj)
        self.Revoke = self._Revoke(websdk_obj=websdk_obj)
        self.Validate = self._Validate(websdk_obj=websdk_obj)

    def Guid(self, guid):
        return self._Guid(guid=guid, websdk_obj=self._api_obj)

    def get(self, limit: int = None, offset: int = None, optional_fields: list = None, filters: dict = None):
        params = {
            'Limit': limit,
            'Offset': offset,
            'OptionalFields': optional_fields
        }.update(filters or {})

        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property()
            def links(self):
                lnks = self._from_json(key='_links')
                return [Certificate.Link(lnk) for lnk in lnks]

            @property
            @json_response_property()
            def x_record_count(self) -> int:
                xrc = self.json_response.headers.get('X-Record-Count')
                return xrc

            @property
            @json_response_property()
            def certificates(self):
                certs = self._from_json(key='Certificates')
                return [Certificate.Certificate(cert) for cert in certs]

            @property
            @json_response_property()
            def data_range(self) -> str:
                return self._from_json(key='DataRange')

            @property
            @json_response_property()
            def total_count(self) -> int:
                return self._from_json(key='TotalCount')

        return _Response(
            response=self._get(params=params),
            expected_return_codes=[200],
            api_source=self._api_source
        )

    class _Associate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Associate')

        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew': push_to_new
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _CheckPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/CheckPolicy')

        def post(self, policy_dn: str, pkcs10: str = None):
            body = {
                'PolicyDN': policy_dn,
                'PKSC10': pkcs10
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def csr(self):
                    return Certificate.CSR(self._from_json(key='CSR', error_key='Error'))

                @property
                @json_response_property()
                def policy(self):
                    return Certificate.Policy(self._from_json(key='Policy'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Dissociate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Dissociate')

        def post(self, certificate_dn: str, application_dn: list, delete_orphans: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Guid(API):
        def __init__(self, guid: str, websdk_obj):
            self._cert_guid = guid
            super().__init__(api_obj=websdk_obj, url='/Certificates/{guid}'.format(guid=self._cert_guid))
            self.PreviousVersions = self._PreviousVersions(guid=self._cert_guid, websdk_obj=websdk_obj)
            self.ValidationResults = self._ValidationResults(guid=self._cert_guid, websdk_obj=websdk_obj)

        def delete(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._delete(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def approver(self) -> List[str]:
                    return self._from_json(key='Approver')

                @property
                @json_response_property()
                def certificate_details(self):
                    return Certificate.CertificateDetails(self._from_json(key='CertificateDetails'))

                @property
                @json_response_property()
                def contact(self) -> List[str]:
                    return self._from_json(key='Contact')

                @property
                @json_response_property()
                def created_on(self):
                    return from_date_string(self._from_json(key='CreatedOn'))

                @property
                @json_response_property()
                def custom_fields(self) -> List[dict]:
                    return self._from_json(key='CustomFields')

                @property
                @json_response_property()
                def dn(self) -> str:
                    return self._from_json(key='DN')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='Guid')

                @property
                @json_response_property()
                def name(self) -> str:
                    return self._from_json(key='Name')

                @property
                @json_response_property()
                def parent_dn(self) -> str:
                    return self._from_json(key='ParentDN')

                @property
                @json_response_property()
                def processing_details(self):
                    return Certificate.ProcessingDetails(self._from_json(key='ProcessingDetails'))

                @property
                @json_response_property()
                def renewal_details(self):
                    return Certificate.RenewalDetails(self._from_json(key='RenewalDetails'))

                @property
                @json_response_property()
                def schema_class(self) -> str:
                    return self._from_json(key='SchemaClass')

                @property
                @json_response_property()
                def success(self) -> str:
                    return self._from_json(key='Success')

                @property
                @json_response_property()
                def validation_details(self):
                    return Certificate.ValidationDetails(self._from_json(key='ValidationDetails'))

            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

        def put(self, attribute_data: [dict]):
            body = {
                "AttributeData": attribute_data
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> str:
                    return self._from_json(key='Success')

            return _Response(
                response=self._put(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

        class _PreviousVersions(API):
            def __init__(self, guid: str, websdk_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=websdk_obj,
                    url='/Certificates/{guid}/PreviousVersions'.format(guid=self._cert_guid)
                )

            def get(self, exclude_expired: bool = False, exclude_revoked: bool = False):
                params = {
                    'ExcludeExpired': exclude_expired,
                    'ExcludeRevoked': exclude_revoked
                }
                
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def success(self) -> bool:
                        return self._from_json(key='Success')

                    @property
                    @json_response_property()
                    def previous_versions(self):
                        return [Certificate.PreviousVersions(version) for version in self._from_json(key='PreviousVersions')]

                return _Response(
                    response=self._get(params=params),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _ValidationResults(API):
            def __init__(self, guid: str, websdk_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=websdk_obj,
                    url='/Certificates/{guid}/ValidationResults'.format(guid=self._cert_guid)
                )

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property(return_on_204=list)
                    def file(self):
                        return [Certificate.File(f) for f in self._from_json(key='File')]

                    @property
                    @json_response_property(return_on_204=list)
                    def ssl_tls(self):
                        return [Certificate.SslTls(s) for s in self._from_json(key='SslTls')]

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200, 204],
                    api_source=self._api_source
                )

    class _Import(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Import')

        def post(self, certificate_data: str, policy_dn: str, ca_specific_attributes: list = None, object_name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
            body = {
                'CertificateData': certificate_data,
                'PolicyDN': policy_dn,
                'CASpecificAttributes': ca_specific_attributes,
                'ObjectName': object_name,
                'Password': password,
                'PrivateKeyData': private_key_data,
                'Reconcile': reconcile
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def certificate_dn(self) -> str:
                    return self._from_json(key='CertificateDN')

                @property
                @json_response_property()
                def certificate_vault_id(self) -> int:
                    return self._from_json(key='CertificateVaultID')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='Guid')

                @property
                @json_response_property()
                def private_key_vault_id(self) -> int:
                    return self._from_json(key='PrivateKeyVaultID')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Push(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='Certificates/Push')

        def post(self, certificate_dn: str, application_dn: List[str] = None, push_to_all: bool = False):
            body = {
                'ApplicationDN': application_dn,
                'CertificateDN': certificate_dn,
                'PushToAll': push_to_all
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(
                        response=response,
                        expected_return_codes=expected_return_codes,
                        api_source=api_source
                    )

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Renew(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Renew')

        def post(self, certificate_dn: str, pkcs10: str = None, reenable: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'PKCS10': pkcs10,
                'Reenable': reenable
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Request(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Request')

        def post(self, policy_dn: str, approvers: [dict] = None, cadn: str = None, ca_specific_attributes: [dict] = None,
                 certificate_type: str = None, city: str = None, contacts: [dict] = None, country: str=None,
                 custom_fields: [dict] = None, created_by: str = None, devices: [dict] = None,
                 disable_automatic_renewal: bool = False, elliptic_curve: str = None, key_algorithm: str = None,
                 key_bit_size: int = None, management_type: str = None, object_name: str = None, organization: str = None,
                 organizational_unit: str = None, pkcs10: str = None, reenable: bool = False, set_work_todo: bool = True,
                 state: str = None, subject: str = None, subject_alt_names: [dict] = None):
            body = {
                'Approvers': approvers,
                'CADN': cadn,
                'CASpecificAttributes': ca_specific_attributes,
                'CertificateType': certificate_type,
                'City': city,
                'Contacts': contacts,
                'Country': country,
                'CustomFields': custom_fields,
                'CreatedBy': created_by,
                'Devices': devices,
                'DisableAutomaticRenewal': disable_automatic_renewal,
                'EllipticCurve': elliptic_curve,
                'KeyAlgorithm': key_algorithm,
                'KeyBitSize': key_bit_size,
                'ManagementType': management_type,
                'ObjectName': object_name,
                'Organization': organization,
                'OrganizationalUnit': organizational_unit,
                'PKCS10': pkcs10,
                'PolicyDN': policy_dn,
                'Reenable': reenable,
                'SetWorkToDo': set_work_todo,
                'State': state,
                'Subject': subject,
                'SubjectAltNames': subject_alt_names
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def certificate_dn(self) -> str:
                    return self._from_json(key='CertificateDN')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='Guid')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Reset(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Reset')

        def post(self, certificate_dn: str, restart: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'Restart': restart
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def private_key_mismatch_reset_completed(self) -> bool:
                    return self._from_json(key='PrivateKeyMismatchResetCompleted')

                @property
                @json_response_property()
                def processing_reset_completed(self) -> bool:
                    return self._from_json(key='ProcessingResetCompleted')

                @property
                @json_response_property()
                def restart_completed(self) -> bool:
                    return self._from_json(key='RestartCompleted')

                @property
                @json_response_property()
                def revocation_reset_completed(self) -> bool:
                    return self._from_json(key='RevocationResetCompleted')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Retrieve(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Retrieve')

        def get(self, certificate_dn: str, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):
            params = {
                'CertificateDN': certificate_dn,
                'Format': format,
                'FriendlyName': friendly_name,
                'IncludeChain': include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword': keystore_password,
                'Password': password,
                'RootFirstOrder': root_first_order
            }

            return APIResponse(
                response=self._get(params=params),
                expected_return_codes=[200],
                api_source=self._api_source
            )

        def post(self, certificate_dn: str, format: str, friendly_name: str, include_chain: bool = False,
                 include_private_key: bool = False, keystore_password: str = None, password: str = None,
                 root_first_order: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'Format': format,
                'FriendlyName': friendly_name,
                'IncludeChain': include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword': keystore_password,
                'Password': password,
                'RootFirstOrder': root_first_order
            }
            
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def certificate_data(self) -> str:
                    return self._from_json(key='CertificateData')

                @property
                @json_response_property()
                def filename(self) -> str:
                    return self._from_json(key='Filename')

                @property
                @json_response_property()
                def format(self) -> str:
                    return self._from_json(key='Format')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

        def VaultId(self, vault_id: int):
            return self._VaultId(vault_id, self._api_source)

        class _VaultId(API):
            def __init__(self, vault_id: int, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/Certificates/Retrieve/{vault_id}'.format(vault_id=vault_id))
                self._vault_id = vault_id

            def get(self, format: str, friendly_name: str, include_chain: bool = False,
                    include_private_key: bool = False, keystore_password: str = None, password: str = None,
                    root_first_order: bool = False):
                params = {
                    'Format': format,
                    'FriendlyName': friendly_name,
                    'IncludeChain': include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword': keystore_password,
                    'Password': password,
                    'RootFirstOrder': root_first_order
                }

                return APIResponse(
                    response=self._get(params=params),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

            def post(self, format: str, friendly_name: str, include_chain: bool = False,
                     include_private_key: bool = False, keystore_password: str = None, password: str = None,
                     root_first_order: bool = False):
                body = {
                    'Format': format,
                    'FriendlyName': friendly_name,
                    'IncludeChain': include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword': keystore_password,
                    'Password': password,
                    'RootFirstOrder': root_first_order
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def certificate_data(self) -> str:
                        return self._from_json(key='CertificateData')

                    @property
                    @json_response_property()
                    def filename(self) -> str:
                        return self._from_json(key='Filename')

                    @property
                    @json_response_property()
                    def format(self) -> str:
                        return self._from_json(key='Format')

                return _Response(
                    response=self._post(data=body),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

    class _Retry(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Retry')

        def post(self, certificate_dn: str):
            body = {
                'CertificateDN': certificate_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Revoke(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Revoke')

        def post(self, certificate_dn: str = None, thumbprint: str = None, reason: str = None, comments: str = None,
                 disable: bool = None):
            body = {
                'CertificateDN': certificate_dn,
                'Thumbprint': thumbprint,
                'Reason': reason,
                'Comments': comments,
                'Disable': disable
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def error(self) -> bool:
                    return self._from_json(key='Error')

                @property
                @json_response_property()
                def requested(self) -> bool:
                    return self._from_json(key='Requested')

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Validate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Certificates/Validate')

        def post(self, certificate_dns: [str] = None, certificate_guids: [str] = None):
            body = {
                'CertificateDNs': certificate_dns,
                'CertificateGUIDs': certificate_guids
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

                @property
                @json_response_property()
                def validated_certificate_dns(self) -> List[str]:
                    return self._from_json(key='ValidatedCertificateDNs')

                @property
                @json_response_property()
                def validated_certificate_guids(self) -> List[str]:
                    return self._from_json(key='ValidatedCertificateGUIDs')

                @property
                @json_response_property()
                def warnings(self) -> List[str]:
                    return self._from_json(key='Warnings')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )
