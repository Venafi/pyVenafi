import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from enums.certificate import CertificateAttributes, CertificateStatus, OptionalFields
from enums.resultcodes import ResultCodes
from objects.response_objects.certificate import Certificate


class _Certificates(API):
    def __init__(self, session, api_type):
        super().__init__(
            session=session,
            api_type=api_type,
            url=WEBSDK_URL + '/Certificates',
            valid_return_codes=[200]
        )
        self.Associate = self._Associate(session, api_type)
        self.CheckPolicy = self._CheckPolicy(session, api_type)
        self.Dissociate = self._Dissociate(session, api_type)
        self.Import = self._Import(session, api_type)
        self.Renew = self._Renew(session, api_type)
        self.Request = self._Request(session, api_type)
        self.Reset = self._Reset(session, api_type)
        self.Retrieve = self._Retrieve(session, api_type)
        self.Retry = self._Retry(session, api_type)
        self.Revoke = self._Revoke(session, api_type)
        self.Validate = self._Validate(session, api_type)

    def Guid(self, guid):
        return self._Guid(guid=guid, session=self._session, api_type=self._api_type)

    @property
    @response_property()
    def links(self):
        lnks = self.response.json()['_links']
        lnks = [Certificate.Link(lnk) for lnk in lnks]
        self.logger.log('_links object created.')
        return lnks

    @property
    @response_property()
    def x_record_count(self):
        xrc = self.response.headers.get('X-Record-Count')
        self.logger.log('Certificates X-Record-Count: %s' % xrc)
        return xrc

    @property
    @response_property()
    def certificates(self):
        certs = self.response.json()['Certificates']
        certs = [Certificate.Certificate(cert) for cert in certs]
        self.logger.log('Certificate objects created.')
        return certs

    @property
    @response_property()
    def data_range(self):
        dr = self.response.json()['DataRange']
        self.logger.log('Certificates DataRange: %s' % dr)
        return dr

    @property
    @response_property()
    def total_count(self):
        tc = self.response.json()['TotalCount']
        self.logger.log('Certificates TotalCount: %s' % tc)
        return tc

    def get(self, limit: int = None, offset: int = None, optional_fields: list = None, filters: dict = None):
        if optional_fields:
            if not isinstance(optional_fields, list):
                optional_fields = [optional_fields]

            if not set(optional_fields).issubset(set(OptionalFields.__dict__.values())):
                raise AssertionError('Invalid option fields. Expected one of {e}, but got {a}. Try importing "enums/certificate.py::OptionalFields".'.format(
                    e=OptionalFields.__dict__.keys(),
                    a=optional_fields
                ))
            optional_fields = ",".join(optional_fields)

        if filters:
            if not (isinstance(filters, dict) and set(filters.keys()).issubset(set(CertificateStatus.__dict__.values()) | set(CertificateAttributes.__dict__.values()))):
                raise TypeError('Filters must be of type dict with keys that map to one or more combinations of certificate attribute filters or '
                                'certificate status filters. Try importing "CertificateStatus" and "CertificateAttributes" from "enums/certificate.py".')

        params = {
            'Limit': limit,
            'Offset': offset,
            'OptionalFields': optional_fields
        }

        params.update(filters)

        self.response = self._session.get(url=self._url, params=params)

        return self

    class _Associate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Associate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def success(self):
            result = self.response.json()['Success']
            if result is False:
                raise ValueError('Associating certificate failed.')
            return result

        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool):
            body = json.dumps({
                'CertiicateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew': push_to_new
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _CheckPolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/CheckPolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def csr(self):
            c = Certificate.CSR(self.response.json()['CSR'])
            self.logger.log('CSR object created successfully.')
            return c

        @property
        @response_property()
        def policy(self):
            p = Certificate.Policy(self.response.json()['Policy'])
            self.logger.log('Certificate Policy object created successfully.')
            return p

        def post(self, policy_dn: str, pkcs10: str = None):
            body = json.dumps({
                'PolicyDN': policy_dn,
                'PKSC10': pkcs10
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Dissociate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Dissociate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def success(self):
            result = self.response.json()['Success']
            if result is False:
                raise ValueError('Dissociating certificate failed.')
            return result

        def post(self, certificate_dn: str, application_dn: list, delete_orphans: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Guid(API):
        def __init__(self, guid: str, session, api_type):
            self._cert_guid = guid
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/{guid}'.format(guid=self._cert_guid),
                valid_return_codes=[200]
            )
            self.PreviousVersions = self._PreviousVersions(self._cert_guid, session, api_type)
            self.ValidationResults = self._ValidationResults(self._cert_guid, session, api_type)

        @property
        @response_property()
        def success(self):
            result = self.response.json()['Success']
            if result is False:
                raise ValueError('Dissociating certificate failed.')
            return result

        @property
        @response_property()
        def approver(self):
            apps = self.response.json()['Approver']
            self.logger.log('Certificate Approvers: %s' % apps)
            return apps

        @property
        @response_property()
        def certificate_details(self):
            details = self.response.json()['CertificateDetails']
            result = Certificate.CertificateDetails(details)
            self.logger.log('Certificate Details object created successfully')
            return result

        @property
        @response_property()
        def contact(self):
            conts = self.response.json()['Contact']
            self.logger.log('Certificate Contacts: %s' % conts)
            return conts

        @property
        @response_property()
        def created_on(self):
            created = self.response.json()['CreatedOn']
            self.logger.log('Certificate CreatedOn: %s' % created)
            return created

        @property
        @response_property()
        def dn(self):
            cert_dn = self.response.json()['DN']
            self.logger.log('Certificate DN: %s' % cert_dn)
            return cert_dn

        @property
        @response_property()
        def guid(self):
            cert_guid = self.response.json()['Guid']
            self.logger.log('Certificate GUID: %s' % cert_guid)
            return cert_guid

        @property
        @response_property()
        def name(self):
            cert_name = self.response.json()['Name']
            self.logger.log('Certificate Name: %s' % cert_name)
            return cert_name

        @property
        @response_property()
        def parent_dn(self):
            pdn = self.response.json()['ParentDn']
            self.logger.log('Certificate Parent DN: %s' % pdn)
            return pdn

        @property
        @response_property()
        def processing_details(self):
            details = self.response.json()['ProcessingDetails']
            result = Certificate.ProcessingDetails(details)
            self.logger.log('Certificate Processing Details object created successfully.')
            return result

        @property
        @response_property()
        def renewal_details(self):
            details = self.response.json()['RenewalDetails']
            result = Certificate.RenewalDetails(details)
            self.logger.log('Certificate Renewal Details object created successfully.')
            return result

        @property
        @response_property()
        def schema_class(self):
            schema = self.response.json()['SchemaClass']
            self.logger.log('Certificate Schema Class: %s' % schema)
            return schema

        @property
        @response_property()
        def validation_details(self):
            details = self.response.json()['ValidationDetails']
            result = Certificate.ValidationDetails(details)
            self.logger.log('Certificate Validation Details object created successfully.')
            return result

        def delete(self):
            self.response = self._session.delete(url=self._url)
            return self

        def get(self):
            self.response = self._session.get(url=self._url)
            return self

        def put(self, attribute_data: [dict]):
            body = json.dumps({
                "AttributeData": attribute_data
            })

            self.response = self._session.put(url=self._url, data=body)
            return self

        class _PreviousVersions(API):
            def __init__(self, guid, session, api_type):
                self._cert_guid = guid
                super().__init__(
                    session=session,
                    api_type=api_type,
                    url=WEBSDK_URL + '/Certificates/{guid}/PreviousVersions'.format(guid=self._cert_guid),
                    valid_return_codes=[200]
                )

            @property
            @response_property()
            def previous_versions(self):
                versions = self.response.json()['PreviousVersions']
                results = [Certificate.PreviousVersions(version) for version in versions]
                self.logger.log('Certificate Previous Versions created successfully.')
                return results

            def get(self, exclude_expired: bool = False, exclude_revoked: bool = False):
                params = {
                    'ExcludeExpired': exclude_expired,
                    'ExcludeRevoked': exclude_revoked
                }
                self.response = self._session.get(url=self._url, params=params)
                return self

        class _ValidationResults(API):
            def __init__(self, guid, session, api_type):
                self._cert_guid = guid
                super().__init__(
                    session=session,
                    api_type=api_type,
                    url=WEBSDK_URL + '/Certificates/{guid}/ValidationResults'.format(guid=self._cert_guid),
                    valid_return_codes=[200, 204]
                )

            @property
            @response_property()
            def file(self):
                files = self.response.json()['File']
                result = [Certificate.File(f) for f in files]
                self.logger.log('Certificate File Validation Results object created successfully.')
                return result

            @property
            @response_property()
            def ssltls(self):
                ssl = self.response.json()['SslTls']
                result = [Certificate.SslTls(s) for s in ssl]
                self.logger.log('Certificate SslTls Validation Results object created successfully.')
                return result

            def get(self):
                self.response = self._session.get(url=self._url)
                return self

    class _Import(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Import',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def certificate_dn(self):
            cdn = self.response.json()['CertificateDN']
            self.logger.log('Certificate DN: %s' % cdn)
            return cdn

        @property
        @response_property()
        def certificate_vault_id(self):
            cvid = self.response.json()['CertificateVaultID']
            self.logger.log('Certificate Vault Id: %s' % cvid)
            return cvid

        @property
        @response_property()
        def guid(self):
            g = self.response.json()['Guid']
            self.logger.log('Certificate Guid: %s' % g)
            return g

        @property
        @response_property()
        def private_key_vault_id(self):
            pkvid = self.response.json()['PrivateKeyVaultId']
            self.logger.log('Certificate Private Key Vault Id: %s' % pkvid)
            return pkvid

        def post(self, certificate_data: str, policy_dn: str, ca_specific_attributes: list = None, object_name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
            body = json.dumps({
                'CertificateData': certificate_data,
                'PolicyDN': policy_dn,
                'CASpecificAttributes': ca_specific_attributes,
                'ObjectName': object_name,
                'Password': password,
                'PrivateKeyData': private_key_data,
                'Reconcile': reconcile
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Renew(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Renew',
                valid_return_codes=[200]
            )

        def post(self, certificate_dn: str, pkcs10: str = None, reenable: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'PKCS10': pkcs10,
                'Reenable': reenable
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Request(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Request',
                valid_return_codes=[200]
            )

        def post(self, policy_dn: str, approvers: [dict] = None, cadn: str = None, ca_specific_attributes: [dict] = None,
                 certificate_type: str = None, city: str = None, contacts: [dict] = None, country: str=None,
                 custom_fields: [dict] = None, created_by: str = None, devices: [dict] = None,
                 disable_automatic_renewal: bool = False, elliptic_curve: str = None, key_algorithm: str = None,
                 key_bit_size: int = None, management_type: str = None, object_name: str = None, organization: str = None,
                 organizational_unit: str = None, pkcs10: str = None, reenable: bool = False, set_work_todo: bool = True,
                 state: str = None, subject: str = None, subject_alt_names: [dict] = None):

            if not(object_name or subject):
                raise ValueError('Cannot request the certificate without either and ObjectName or Subject.')

            body = json.dumps({
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
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Reset(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Reset',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def private_key_mismatch_reset_completed(self):
            result = self.response.json()['PrivateKeyMismatchResetCompleted']
            self.logger.log('PrivateKeyMismatchResetCompleted: %s' % result)
            return result

        @property
        @response_property()
        def processing_reset_completed(self):
            result = self.response.json()['ProcessingResetCompleted']
            self.logger.log('ProcessingResetCompleted: %s' % result)
            return result

        @property
        @response_property()
        def restart_completed(self):
            result = self.response.json()['RestartCompleted']
            self.logger.log('RestartCompleted: %s' % result)
            return result

        @property
        @response_property()
        def revocation_reset_completed(self):
            result = self.response.json()['RevocationResetCompleted']
            self.logger.log('RevocationResetCompleted: %s' % result)
            return result

        def post(self, certificate_dn: str, restart: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'Restart': restart
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Retrieve(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Retrieve',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def certificate_data(self):
            cd = self.response.json()['CertificateData']
            self.logger.log('Certificate Data: %s' % cd)
            return cd

        @property
        @response_property()
        def filename(self):
            f = self.response.json()['Filename']
            self.logger.log('Certificate Filename: %s' % f)
            return f

        @property
        @response_property()
        def format(self):
            f = self.response.json()['Format']
            self.logger.log('Certificate Format: %s' % f)
            return f

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

            self.response = self._session.get(url=self._url, params=params)
            return self

        def post(self, certificate_dn: str, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'Format': format,
                'FriendlyName': friendly_name,
                'IncludeChain': include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword': keystore_password,
                'Password': password,
                'RootFirstOrder': root_first_order
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

        def VaultId(self, vault_id: int):
            return self._VaultId(vault_id, self._session, self._api_type)

        class _VaultId(API):
            def __init__(self, vault_id, session, api_type):
                super().__init__(
                    session=session,
                    api_type=api_type,
                    url=WEBSDK_URL + '/Certificates/Retrieve/{vault_id}'.format(vault_id=vault_id),
                    valid_return_codes=[200]
                )
                self._vault_id = vault_id

            @property
            @response_property()
            def certificate_data(self):
                cd = self.response.json()['CertificateData']
                self.logger.log('Certificate Data: %s' % cd)
                return cd

            @property
            @response_property()
            def filename(self):
                f = self.response.json()['Filename']
                self.logger.log('Certificate Filename: %s' % f)
                return f

            @property
            @response_property()
            def format(self):
                f = self.response.json()['Format']
                self.logger.log('Certificate Format: %s' % f)
                return f

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

                self.response = self._session.get(url=self._url, params=params)
                return self

            def post(self, format: str, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False):

                body = json.dumps({
                    'Format': format,
                    'FriendlyName': friendly_name,
                    'IncludeChain': include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword': keystore_password,
                    'Password': password,
                    'RootFirstOrder': root_first_order
                })

                self.response = self._session.post(url=self._url, data=body)
                return self

    class _Retry(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Retry',
                valid_return_codes=[200]
            )

        def post(self, certificate_dn: str):
            body = json.dumps({
                'CertificateDN': certificate_dn
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Revoke(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Revoke',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def requested(self):
            req = self.response.json()['Requested']
            self.logger.log('Requested: %s' % req)
            return req

        def post(self, certificate_dn: str = None, thumbprint: str = None, reason: str = None, comments: str = None,
                 disable: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'Thumbprint': thumbprint,
                'Reason': reason,
                'Comments': comments,
                'Disable': disable
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Validate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Validate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def validated_certificate_dns(self):
            dns = self.response.json()['ValidatedCertificateDNs']
            self.logger.log('Validated Certificate DNs: %s' % dns)
            return dns

        @property
        @response_property()
        def validated_certificate_guids(self):
            guids = self.response.json()['ValidatedCertificateGUIDs']
            self.logger.log('Validated Certificate GUIDs: %s' % guids)
            return guids

        @property
        @response_property()
        def warnings(self):
            w = self.response.json()['Warnings']
            self.logger.log('Validation Warnings: %s' % w)
            return w

        def post(self, certificate_dns: [str] = None, certificate_guids: [str] = None):
            if not(certificate_dns or certificate_guids):
                raise ValueError('Must supply either a list of Certificate DNs or Certificate GUIDs to validate.')

            body = json.dumps({
                'CertificateDNs': certificate_dns,
                'CertificateGUIDs': certificate_guids
            })

            self.response = self._session.post(url=self._url, data=body)
            return self
