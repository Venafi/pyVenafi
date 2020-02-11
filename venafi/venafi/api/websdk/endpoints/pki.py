from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.pki import PKI


class _PKI:
    def __init__(self, websdk_obj):
        self.HashiCorp = self._HashiCorp(websdk_obj=websdk_obj)

    class _HashiCorp:
        def __init__(self, websdk_obj):
            self.CA = self._CA(websdk_obj=websdk_obj)

        class _CA(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/HashiCorp/CA', valid_return_codes=[200])
                self._websdk_obj = websdk_obj

            def Guid(self, guid: str):
                return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

            @property
            @json_response_property()
            def certificate_dn(self) -> str:
                return self._from_json(key='CertificateDN')
            
            @property
            @json_response_property()
            def certificate_guid(self) -> str:
                return self._from_json(key='CertificateGuid')

            @property
            @json_response_property()
            def error(self) -> str:
                return self._from_json(key='Error')

            @property
            @json_response_property()
            def guid(self) -> str:
                return self._from_json(key='Guid')

            @property
            @json_response_property()
            def pkis(self):
                return [PKI.PKI(pki) for pki in self._from_json(key='pkis')]

            def get(self):
                self.json_response = self._get()

            def post(self, certificate: dict, folder_dn: str, pki_path: str, roles: List[str],
                     create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                     installation: dict = None, key_algorithm: str = None, key_bit_size: str = None, ocsp_address: str = None):
                body = {
                    'Certificate': certificate,
                    'CreateCertificateAuthority': create_certificate_authority,
                    'CreatePKIRole': create_pki_role,
                    'CRLAddress': crl_address,
                    'FolderDn': folder_dn,
                    'Installation': installation,
                    'KeyAlgorithm': key_algorithm,
                    'KeyBitSize': key_bit_size,
                    'OCSPAddress': ocsp_address,
                    'PkiPath': pki_path,
                    'Roles': roles
                }

                self.json_response = self._post(data=body)
                return self

            class _Guid(API):
                def __init__(self, guid: str, websdk_obj):
                    super().__init__(api_obj=websdk_obj, url=f'/HashiCorp/CA/{guid}', valid_return_codes=[200])
                    self._guid = guid
                    self.Renew = self._Renew(guid=guid, websdk_obj=websdk_obj)

                @property
                @json_response_property()
                def certificate(self):
                    return PKI.Certificate(self._from_json(key='Certificate'))

                @property
                @json_response_property()
                def certificate_dn(self) -> str:
                    return self._from_json(key='CertificateDN')

                @property
                @json_response_property()
                def certificate_guid(self) -> str:
                    return self._from_json(key='CertificateGuid')

                @property
                @json_response_property()
                def create_certificate_authority(self) -> bool:
                    return self._from_json(key='CreateCertificateAuthority')

                @property
                @json_response_property()
                def create_pki_role(self) -> bool:
                    return self._from_json(key='CreatePKIRole')

                @property
                @json_response_property()
                def error(self) -> str:
                    return self._from_json(key='Error')

                @property
                @json_response_property()
                def folder_dn(self):
                    return self._from_json(key='FolderDn')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='Guid')

                @property
                @json_response_property()
                def installation(self):
                    return PKI.Installation(self._from_json(key='Installation'))

                @property
                @json_response_property()
                def pki_path(self):
                    return self._from_json(key='PkiPath')

                @property
                @json_response_property()
                def roles(self) -> list:
                    return self._from_json(key='Roles')

                def delete(self):
                    self.json_response = self._delete()
                    return self

                def get(self):
                    self.json_response = self._get()
                    return self

                def post(self):
                    self.json_response = self._post(data={})
                    return self

                def put(self, folder_dn: str, pki_path: str, roles: List[str], certificate: dict = None,
                        create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                        installation: dict = None, key_algorithm: str = None, key_bit_size: str = None, ocsp_address: str = None):
                    body = {
                        'Certificate': certificate,
                        'CreateCertificateAuthority': create_certificate_authority,
                        'CreatePKIRole': create_pki_role,
                        'CRLAddress': crl_address,
                        'FolderDn': folder_dn,
                        'Installation': installation,
                        'KeyAlgorithm': key_algorithm,
                        'KeyBitSize': key_bit_size,
                        'OCSPAddress': ocsp_address,
                        'PkiPath': pki_path,
                        'Roles': roles
                    }

                    self.json_response = self._put(data=body)
                    return self

                class _Renew(API):
                    def __init__(self, guid:str, websdk_obj):
                        super().__init__(api_obj=websdk_obj, url=f'HashiCorp/{guid}/Renew', valid_return_codes=[200])

                    @property
                    @json_response_property()
                    def certificate_dn(self) -> str:
                        return self._from_json(key='CertificateDN')

                    @property
                    @json_response_property()
                    def certificate_guid(self) -> str:
                        return self._from_json(key='CertificateGuid')

                    @property
                    @json_response_property()
                    def guid(self) -> str:
                        return self._from_json(key='Guid')

                    def post(self):
                        self.json_response = self._post(data={})
                        return self

        class _Role(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='HashiCorp/Role', valid_return_codes=[200])
                self._websdk_obj = websdk_obj

            @property
            @json_response_property()
            def error(self) -> str:
                return self._from_json(key='Error')

            @property
            @json_response_property()
            def guid(self) -> str:
                return self._from_json(key='Guid')

            def post(self, folder_dn: str, role_name: str, city: str = None, country: str = None,
                     enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                     organization: str = None, organizational_units: List[str] = None, state: str = None,
                     whitelisted_domains: List[str] = None):
                body = {
                    'City': city,
                    'Country': country,
                    'EnhancedKeyUsage': enhanced_key_usage,
                    'FolderDn': folder_dn,
                    'KeyAlgorithm': key_algorithm,
                    'KeyBitSize': key_bit_size,
                    'Organization': organization,
                    'OrganizationalUnits': organizational_units,
                    'RoleName': role_name,
                    'State': state,
                    'WhitelistedDomains': whitelisted_domains
                }

                self.json_response = self._post(data=body)
                return self

            def Guid(self, guid: str):
                return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

            class _Guid(API):
                def __init__(self, guid: str, websdk_obj):
                    super().__init__(api_obj=websdk_obj, url=f'HashiCorp/Role/{guid}', valid_return_codes=[200])

                @property
                @json_response_property()
                def city(self) -> str:
                    return self._from_json(key='City')

                @property
                @json_response_property()
                def country(self) -> str:
                    return self._from_json(key='Country')

                @property
                @json_response_property()
                def enhanced_key_usage(self) -> str:
                    return self._from_json(key='EnhancedKeyUsage')
                
                @property
                @json_response_property()
                def error(self) -> str:
                    return self._from_json(key='Error')
                
                @property
                @json_response_property()
                def folder_dn(self) -> str:
                    return self._from_json(key='FolderDn')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='Guid')
                
                @property
                @json_response_property()
                def key_algorithm(self) -> str:
                    return self._from_json(key='KeyAlgorithm')
                
                @property
                @json_response_property()
                def key_bit_size(self) -> str:
                    return self._from_json(key='KeyBitSize')
                
                @property
                @json_response_property()
                def organization(self) -> str:
                    return self._from_json(key='Organization')
                
                @property
                @json_response_property()
                def organizational_units(self) -> List[str]:
                    return self._from_json(key='OrganizationalUnits')
                
                @property
                @json_response_property()
                def role_name(self) -> str:
                    return self._from_json(key='RoleName')
                
                @property
                @json_response_property()
                def state(self) -> str:
                    return self._from_json(key='State')
                
                @property
                @json_response_property()
                def whitelisted_domains(self) -> List[str]:
                    return self._from_json(key='WhitelistedDomains')

                def delete(self):
                    self.json_response = self._delete()
                    return self

                def get(self):
                    self.json_response = self._get()
                    return self

                def put(self, city: str = None, country: str = None,
                        enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                        organization: str = None, organizational_units: List[str] = None, state: str = None,
                        whitelisted_domains: List[str] = None):
                    body = {
                        'City': city,
                        'Country': country,
                        'EnhancedKeyUsage': enhanced_key_usage,
                        'KeyAlgorithm': key_algorithm,
                        'KeyBitSize': key_bit_size,
                        'Organization': organization,
                        'OrganizationalUnits': organizational_units,
                        'State': state,
                        'WhitelistedDomains': whitelisted_domains
                    }

                    self.json_response = self._put(data=body)
                    return self
