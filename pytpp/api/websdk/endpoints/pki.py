from typing import List
from properties.response_objects.dataclasses import pki
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _PKI:
    def __init__(self, api_obj):
        self.HashiCorp = self._HashiCorp(api_obj=api_obj)

    class _HashiCorp:
        def __init__(self, api_obj):
            self.CA = self._CA(api_obj=api_obj)
            self.Role = self._Role(api_obj=api_obj)

        class _CA(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/HashiCorp/CA')
                self._api_obj = api_obj

            def Guid(self, guid: str):
                return self._Guid(guid=guid, api_obj=self._api_obj)

            def get(self):
                class Response(APIResponse):
                    pkis : List[pki.PKI] = ResponseField(default_factory=list, alias='pkis')

                return ResponseFactory(response_cls=Response, response=self._get())

            def post(self, certificate: dict, folder_dn: str, pki_path: str, roles: List[str],
                     create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                     installation: dict = None, key_algorithm: str = None, key_bit_size: str = None, ocsp_address: str = None):
                body = {
                    'Certificate'               : certificate,
                    'CreateCertificateAuthority': create_certificate_authority,
                    'CreatePKIRole'             : create_pki_role,
                    'CRLAddress'                : crl_address,
                    'FolderDn'                  : folder_dn,
                    'Installation'              : installation,
                    'KeyAlgorithm'              : key_algorithm,
                    'KeyBitSize'                : key_bit_size,
                    'OCSPAddress'               : ocsp_address,
                    'PkiPath'                   : pki_path,
                    'Roles'                     : roles
                }

                class Response(APIResponse):
                    certificate_dn: str = ResponseField(alias='CertificateDN')
                    certificate_guid: str = ResponseField(alias='CertificateGuid')
                    guid: str = ResponseField(alias='Guid')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

            class _Guid(API):
                def __init__(self, guid: str, api_obj):
                    super().__init__(api_obj=api_obj, url=f'/HashiCorp/CA/{guid}')
                    self._guid = guid
                    self.Renew = self._Renew(guid=guid, api_obj=api_obj)

                def delete(self):
                    class Response(APIResponse):
                        certificate_dn: str = ResponseField(alias='CertificateDN')
                        certificate_guid: str = ResponseField(alias='CertificateGuid')
                        guid: str = ResponseField(alias='Guid')

                    return ResponseFactory(response_cls=Response, response=self._delete())

                def get(self):
                    class Response(APIResponse):
                        certificate : pki.Certificate = ResponseField(alias='Certificate')
                        create_certificate_authority: bool = ResponseField(alias='CreateCertificateAuthority')
                        create_pki_role: bool = ResponseField(alias='CreatePKIRole')
                        folder_dn: str = ResponseField(alias='FolderDn')
                        installation: pki.Installation = ResponseField(alias='Installation')
                        pki_path: str = ResponseField(alias='PkiPath')
                        roles: list = ResponseField(alias='Roles')

                    return ResponseFactory(response_cls=Response, response=self._get())

                def post(self):
                    class Response(APIResponse):
                        certificate_dn: str = ResponseField(alias='CertificateDN')
                        certificate_guid: str = ResponseField(alias='CertificateGuid')
                        guid: str = ResponseField(alias='Guid')

                    return ResponseFactory(response_cls=Response, response=self._post(data={}))

                def put(self, folder_dn: str, pki_path: str, roles: List[str], certificate: dict = None,
                        create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                        installation: dict = None, key_algorithm: str = None, key_bit_size: str = None, ocsp_address: str = None):
                    body = {
                        'Certificate'               : certificate,
                        'CreateCertificateAuthority': create_certificate_authority,
                        'CreatePKIRole'             : create_pki_role,
                        'CRLAddress'                : crl_address,
                        'FolderDn'                  : folder_dn,
                        'Installation'              : installation,
                        'KeyAlgorithm'              : key_algorithm,
                        'KeyBitSize'                : key_bit_size,
                        'OCSPAddress'               : ocsp_address,
                        'PkiPath'                   : pki_path,
                        'Roles'                     : roles
                    }

                    class Response(APIResponse):
                        certificate_dn: str = ResponseField(alias='CertificateDN')
                        certificate_guid: str = ResponseField(alias='CertificateGuid')
                        guid: str = ResponseField(alias='Guid')

                    return ResponseFactory(response_cls=Response, response=self._put(data=body))

                class _Renew(API):
                    def __init__(self, guid: str, api_obj):
                        super().__init__(api_obj=api_obj, url=f'HashiCorp/{guid}/Renew')

                    def post(self):
                        class Response(APIResponse):
                            certificate_dn: str = ResponseField(alias='CertificateDN')
                            certificate_guid: str = ResponseField(alias='CertificateGuid')
                            guid: str = ResponseField(alias='Guid')

                        return ResponseFactory(response_cls=Response, response=self._post(data={}))

        class _Role(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='HashiCorp/Role')
                self._api_obj = api_obj

            def post(self, folder_dn: str, role_name: str, city: str = None, country: str = None,
                     enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                     organization: str = None, organizational_units: List[str] = None, state: str = None,
                     whitelisted_domains: List[str] = None):
                body = {
                    'City'               : city,
                    'Country'            : country,
                    'EnhancedKeyUsage'   : enhanced_key_usage,
                    'FolderDn'           : folder_dn,
                    'KeyAlgorithm'       : key_algorithm,
                    'KeyBitSize'         : key_bit_size,
                    'Organization'       : organization,
                    'OrganizationalUnits': organizational_units,
                    'RoleName'           : role_name,
                    'State'              : state,
                    'WhitelistedDomains' : whitelisted_domains
                }

                class Response(APIResponse):
                    guid: str = ResponseField(alias='Guid')

                return ResponseFactory(response_cls=Response, response=self._post(data=body))

            def Guid(self, guid: str):
                return self._Guid(guid=guid, api_obj=self._api_obj)

            class _Guid(API):
                def __init__(self, guid: str, api_obj):
                    super().__init__(api_obj=api_obj, url=f'HashiCorp/Role/{guid}')

                def delete(self):
                    class Response(APIResponse):
                        guid: str = ResponseField(alias='Guid')

                    return ResponseFactory(response_cls=Response, response=self._delete())

                def get(self):
                    class Response(APIResponse):
                        city: str = ResponseField(alias='City')
                        country: str = ResponseField(alias='Country')
                        enhanced_key_usage: str = ResponseField(alias='EnhancedKeyUsage')
                        folder_dn: str = ResponseField(alias='FolderDn')
                        guid: str = ResponseField(alias='Guid')
                        key_algorithm: str = ResponseField(alias='KeyAlgorithm')
                        key_bit_size: str = ResponseField(alias='KeyBitSize')
                        organization: str = ResponseField(alias='Organization')
                        organizational_units: List[str] = ResponseField(default_factory=list, alias='OrganizationalUnits')
                        role_name: str = ResponseField(alias='RoleName')
                        state: str = ResponseField(alias='State')
                        whitelisted_domains: List[str] = ResponseField(default_factory=list, alias='WhitelistedDomains')

                    return ResponseFactory(response_cls=Response, response=self._get())

                def put(self, city: str = None, country: str = None,
                        enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                        organization: str = None, organizational_units: List[str] = None, state: str = None,
                        whitelisted_domains: List[str] = None):
                    body = {
                        'City'               : city,
                        'Country'            : country,
                        'EnhancedKeyUsage'   : enhanced_key_usage,
                        'KeyAlgorithm'       : key_algorithm,
                        'KeyBitSize'         : key_bit_size,
                        'Organization'       : organization,
                        'OrganizationalUnits': organizational_units,
                        'State'              : state,
                        'WhitelistedDomains' : whitelisted_domains
                    }

                    class Response(APIResponse):
                        guid: str = ResponseField(alias='Guid')

                    return ResponseFactory(response_cls=Response, response=self._put(data=body))
