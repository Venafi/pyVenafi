from datetime import datetime
from typing import List
from pytpp.api.websdk.outputs import certificate
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Certificates(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Certificates')
        self.Associate = self._Associate(api_obj=api_obj)
        self.CheckPolicy = self._CheckPolicy(api_obj=api_obj)
        self.Dissociate = self._Dissociate(api_obj=api_obj)
        self.Import = self._Import(api_obj=api_obj)
        self.Push = self._Push(api_obj=api_obj)
        self.Renew = self._Renew(api_obj=api_obj)
        self.Request = self._Request(api_obj=api_obj)
        self.Reset = self._Reset(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Retry = self._Retry(api_obj=api_obj)
        self.Revoke = self._Revoke(api_obj=api_obj)
        self.Validate = self._Validate(api_obj=api_obj)

    def Guid(self, guid):
        return self._Guid(guid=guid, api_obj=self._api_obj)

    def get(self, limit: int = None, offset: int = None, optional_fields: list = None, filters: dict = None):
        params = {
            'Limit'         : limit,
            'Offset'        : offset,
            'OptionalFields': optional_fields
        }
        params.update(filters or {})

        class Response(WebSdkOutputModel):
            links: List[certificate.Link] = ApiField(default_factory=list, alias='_links')
            x_record_count: int = ApiField(alias='X-Record-Count')
            certificates: List[certificate.Certificate] = ApiField(default_factory=list, alias='Certificates')
            data_range: str = ApiField(alias='DataRange')
            total_count: int = ApiField(alias='TotalCount')

        return generate_output(response=self._get(params=params), response_cls=Response)

    def head(self, filters: dict = None):
        params = filters

        class Response(WebSdkOutputModel):
            @property
            def x_record_count(self):
                xrc = int(self.api_response.headers.get('X-Record-Count'))
                return xrc

        return generate_output(response=self._get(params=params), response_cls=Response)

    class _Associate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Associate')

        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew'    : push_to_new
            }

            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _CheckPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/CheckPolicy')

        def post(self, policy_dn: str, pkcs10: str = None):
            body = {
                'PolicyDN': policy_dn,
                'PKSC10'  : pkcs10
            }

            class Response(WebSdkOutputModel):
                csr: certificate.CSR = ApiField(alias='CSR')
                policy: certificate.Policy = ApiField(alias='Policy')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Dissociate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Dissociate')

        def post(self, certificate_dn: str, application_dn: List[str], delete_orphans: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            }

            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Guid(WebSdkEndpoint):
        def __init__(self, guid: str, api_obj):
            self._cert_guid = guid
            super().__init__(api_obj=api_obj, url='/Certificates/{guid}'.format(guid=self._cert_guid))
            self.PreviousVersions = self._PreviousVersions(guid=self._cert_guid, api_obj=api_obj)
            self.ValidationResults = self._ValidationResults(guid=self._cert_guid, api_obj=api_obj)

        def delete(self):
            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._delete(), response_cls=Response)

        def get(self):
            class Response(WebSdkOutputModel):
                approver: List[str] = ApiField(default_factory=list, alias='Approver')
                certificate_authority_dn: datetime = ApiField(alias='CertificateAuthorityDN')
                certificate_details: certificate.CertificateDetails = ApiField(default_factory=None, alias='CertificateDetails')
                consumers: List[str] = ApiField(alias='Consumers', default_factory=list)
                contact: List[str] = ApiField(default_factory=list, alias='Contact')
                created_by: str = ApiField(alias='CreatedBy')
                created_on: datetime = ApiField(alias='CreatedOn')
                custom_fields: List[certificate.NameTypeValue] = ApiField(default_factory=list, alias='CustomFields')
                disabled: bool = ApiField(alias='Disabled')
                dn: str = ApiField(alias='DN')
                guid: str = ApiField(alias='Guid')
                management_type: str = ApiField(alias='ManagementType')
                name: str = ApiField(alias='Name')
                parent_dn: str = ApiField(alias='ParentDN')
                processing_details: certificate.ProcessingDetails = ApiField(alias='ProcessingDetails')
                renewal_details: certificate.RenewalDetails = ApiField(alias='RenewalDetails')
                schema_class: str = ApiField(alias='SchemaClass')
                success: str = ApiField(alias='Success')
                validation_details: certificate.ValidationDetails = ApiField(alias='ValidationDetails')

            return generate_output(response=self._get(), response_cls=Response)

        def put(self, attribute_data: List[dict]):
            body = {
                "AttributeData": attribute_data
            }

            class Response(WebSdkOutputModel):
                success: str = ApiField(alias='Success')

            return generate_output(response=self._put(data=body), response_cls=Response)

        class _PreviousVersions(WebSdkEndpoint):
            def __init__(self, guid: str, api_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=api_obj,
                    url='/Certificates/{guid}/PreviousVersions'.format(guid=self._cert_guid)
                )

            def get(self, exclude_expired: bool = False, exclude_revoked: bool = False):
                params = {
                    'ExcludeExpired': exclude_expired,
                    'ExcludeRevoked': exclude_revoked
                }

                class Response(WebSdkOutputModel):
                    success: str = ApiField(default='', alias='Success')
                    previous_versions: List[certificate.PreviousVersions] = ApiField(
                        default_factory=list, alias='PreviousVersions'
                    )

                return generate_output(response=self._get(params=params), response_cls=Response)

        class _ValidationResults(WebSdkEndpoint):
            def __init__(self, guid: str, api_obj):
                self._cert_guid = guid
                super().__init__(
                    api_obj=api_obj,
                    url='/Certificates/{guid}/ValidationResults'.format(guid=self._cert_guid)
                )

            def get(self):
                class Response(WebSdkOutputModel):
                    file: List[certificate.File] = ApiField(default_factory=list, alias='File')
                    ssl_tls: List[certificate.SslTls] = ApiField(default_factory=list, alias='SslTls')

                return generate_output(response=self._get(), response_cls=Response)

    class _Import(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Import')

        def post(self, certificate_data: str, policy_dn: str, ca_specific_attributes: list = None, object_name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
            body = {
                'CertificateData'     : certificate_data,
                'PolicyDN'            : policy_dn,
                'CASpecificAttributes': ca_specific_attributes,
                'ObjectName'          : object_name,
                'Password'            : password,
                'PrivateKeyData'      : private_key_data,
                'Reconcile'           : reconcile
            }

            class Response(WebSdkOutputModel):
                certificate_dn: str = ApiField(alias='CertificateDN')
                certificate_vault_id: int = ApiField(alias='CertificateVaultID')
                guid: str = ApiField(alias='Guid')
                private_key_vault_id: int = ApiField(alias='PrivateKeyVaultID')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Push(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Certificates/Push')

        def post(self, certificate_dn: str, application_dn: List[str] = None, push_to_all: bool = False):
            body = {
                'ApplicationDN': application_dn,
                'CertificateDN': certificate_dn,
                'PushToAll'    : push_to_all
            }

            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Renew(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Renew')

        # noinspection ALL
        def post(self, certificate_dn: str, pkcs10: str = None, reenable: bool = False, format: certificate.CertificateFormat = None,
                 password: str = None, include_private_key: bool = None, include_chain: bool = None,
                 friendly_name: str = None, root_first_order: bool = None, keystore_password: str = None,
                 work_to_do_timeout: int = None):
            body = {
                'CertificateDN'    : certificate_dn,
                'PKCS10'           : pkcs10,
                'Reenable'         : reenable,
                'Format'           : format,
                'Password'         : password,
                'IncludePrivateKey': include_private_key,
                'IncludeChain'     : include_chain,
                'FriendlyName'     : friendly_name,
                'RootFirstOrder'   : root_first_order,
                'KeystorePassword' : keystore_password,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                certificate_dn: str = ApiField(alias='CertificateDN')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Request(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Request')

        def post(self, policy_dn: str, approvers: List[dict] = None, cadn: str = None,
                 ca_specific_attributes: List[dict] = None, certificate_type: str = None, city: str = None,
                 contacts: List[dict] = None, country: str = None, custom_fields: List[dict] = None, created_by: str = None,
                 devices: List[dict] = None, disable_automatic_renewal: bool = False, elliptic_curve: str = None,
                 format: certificate.CertificateFormat = None, friendly_name: str = None, include_private_key: bool = False,
                 include_chain: bool = None, key_algorithm: str = None, key_bit_size: int = None, keystore_password: str = None,
                 management_type: str = None, password: str = None, object_name: str = None,
                 organization: str = None, organizational_unit: str = None, origin: str = None, pkcs10: str = None,
                 reenable: bool = False, root_first_order: bool = None, set_work_todo: bool = True, state: str = None,
                 subject: str = None, subject_alt_names: List[dict] = None, work_to_do_timeout: int = None):
            body = {
                'Approvers'              : approvers,
                'CADN'                   : cadn,
                'CASpecificAttributes'   : ca_specific_attributes,
                'CertificateType'        : certificate_type,
                'City'                   : city,
                'Contacts'               : contacts,
                'Country'                : country,
                'CustomFields'           : custom_fields,
                'CreatedBy'              : created_by,
                'Devices'                : devices,
                'DisableAutomaticRenewal': disable_automatic_renewal,
                'EllipticCurve'          : elliptic_curve,
                'Format'                 : format,
                'FriendlyName'           : friendly_name,
                'IncludePrivateKey'      : include_private_key,
                'IncludeChain'           : include_chain,
                'KeystorePassword'       : keystore_password,
                'KeyAlgorithm'           : key_algorithm,
                'KeyBitSize'             : key_bit_size,
                'ManagementType'         : management_type,
                'ObjectName'             : object_name,
                'Origin'                 : origin,
                'Organization'           : organization,
                'OrganizationalUnit'     : organizational_unit,
                'Password'               : password,
                'PKCS10'                 : pkcs10,
                'PolicyDN'               : policy_dn,
                'Reenable'               : reenable,
                'RootFirstOrder'         : root_first_order,
                'SetWorkToDo'            : set_work_todo,
                'State'                  : state,
                'Subject'                : subject,
                'SubjectAltNames'        : subject_alt_names,
                'WorkToDoTimeout'        : work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')
                certificate_dn: str = ApiField(alias='CertificateDN')
                guid: str = ApiField(alias='Guid')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Reset(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Reset')

        def post(self, certificate_dn: str, restart: bool = False, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'Restart'        : restart,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                private_key_mismatch_reset_completed: bool = ApiField(alias='PrivateKeyMismatchResetCompleted')
                processing_reset_completed: bool = ApiField(alias='ProcessingResetCompleted')
                restart_completed: bool = ApiField(alias='RestartCompleted')
                revocation_reset_completed: bool = ApiField(alias='RevocationResetCompleted')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Retrieve(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Retrieve')

        # noinspection ALL
        def get(self, certificate_dn: str, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False, work_to_do_timeout: int = None):
            params = {
                'CertificateDN'    : certificate_dn,
                'Format'           : format,
                'FriendlyName'     : friendly_name,
                'IncludeChain'     : include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword' : keystore_password,
                'Password'         : password,
                'RootFirstOrder'   : root_first_order,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            return generate_output(response=self._get(params=params), response_cls=WebSdkOutputModel)

        def post(self, certificate_dn: str, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                 include_private_key: bool = False, keystore_password: str = None, password: str = None,
                 root_first_order: bool = False, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'    : certificate_dn,
                'Format'           : format,
                'FriendlyName'     : friendly_name,
                'IncludeChain'     : include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword' : keystore_password,
                'Password'         : password,
                'RootFirstOrder'   : root_first_order,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')

            return generate_output(response=self._post(data=body), response_cls=Response)

        def VaultId(self, vault_id: int):
            return self._VaultId(vault_id=vault_id, api_obj=self._api_obj)

        class _VaultId(WebSdkEndpoint):
            def __init__(self, vault_id: int, api_obj):
                super().__init__(api_obj=api_obj, url='/Certificates/Retrieve/{vault_id}'.format(vault_id=vault_id))
                self._vault_id = vault_id

            # noinspection ALL
            def get(self, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                    include_private_key: bool = False, keystore_password: str = None, password: str = None,
                    root_first_order: bool = False):
                params = {
                    'Format'           : format,
                    'FriendlyName'     : friendly_name,
                    'IncludeChain'     : include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword' : keystore_password,
                    'Password'         : password,
                    'RootFirstOrder'   : root_first_order
                }

                return generate_output(response=self._get(params=params), response_cls=WebSdkOutputModel)

            # noinspection ALL
            def post(self, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                     include_private_key: bool = False, keystore_password: str = None, password: str = None,
                     root_first_order: bool = False):
                body = {
                    'Format'           : format,
                    'FriendlyName'     : friendly_name,
                    'IncludeChain'     : include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword' : keystore_password,
                    'Password'         : password,
                    'RootFirstOrder'   : root_first_order
                }

                class Response(WebSdkOutputModel):
                    certificate_data: str = ApiField(alias='CertificateData')
                    filename: str = ApiField(alias='Filename')
                    format: certificate.CertificateFormat = ApiField(alias='Format')

                return generate_output(response=self._post(data=body), response_cls=Response)

    class _Retry(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Retry')

        def post(self, certificate_dn: str, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Revoke(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Revoke')

        def post(self, certificate_dn: str = None, thumbprint: str = None, reason: int = None, comments: str = None,
                 disable: bool = None, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'Thumbprint'     : thumbprint,
                'Reason'         : reason,
                'Comments'       : comments,
                'Disable'        : disable,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Response(WebSdkOutputModel):
                requested: bool = ApiField(alias='Requested')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Validate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Certificates/Validate')

        def post(self, certificate_dns: List[str] = None, certificate_guids: List[str] = None):
            body = {
                'CertificateDNs'  : certificate_dns,
                'CertificateGUIDs': certificate_guids
            }

            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                validated_certificate_dns: List[str] = ApiField(default_factory=list, alias='ValidatedCertificateDNs')
                validated_certificate_guids: List[str] = ApiField(default_factory=list, alias='ValidatedCertificateGUIDs')
                warnings: List[str] = ApiField(default_factory=list, alias='Warnings')

            return generate_output(response=self._post(data=body), response_cls=Response)
