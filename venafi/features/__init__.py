from venafi.features.bases.feature_base import FeatureBase
from venafi.features.attributes import Attributes
from venafi.features.folder import Folder, FolderAttributes, FolderClassNames
from venafi.features.certificate import Certificate, CertificateAttributes, CertificateClassNames
from venafi.features.device import Device, DeviceAttributes, DevicesClassNames
from venafi.features.application import Apache, PKCS11, ApplicationAttributes, ApplicationAttributeValues, \
    ApplicationClassNames
from venafi.features.credentials import AmazonCredential, CertificateCredential, GenericCredential, \
    PasswordCredential, PrivateKeyCredential, UsernamePasswordCredential, CredentialAttributes
from venafi.features.certificate_authorities import MSCA, SelfSigned, CertificateAuthorityAttributes, \
    CertificateAuthorityClassNames


class Features(FeatureBase):
    class _Applications:
        def __init__(self, auth):
            self.auth = auth

            self._apache = None
            self._pkcs11 = None

        @property
        def apache(self):
            self._apache = self._apache or Apache(self.auth)
            return self._apache

        @property
        def pkcs11(self):
            self._pkcs11 = self._pkcs11 or PKCS11(self.auth)
            return self._pkcs11

    class _CertificateAuthorities:
        def __init__(self, auth):
            self.auth = auth

            self._msca = None
            self._self_signed = None

        @property
        def msca(self):
            self._msca = self._msca or MSCA(self.auth)
            return self._msca

        @property
        def self_signed(self):
            self._self_signed = self._self_signed or SelfSigned(self.auth)
            return self._self_signed

    class _Credentials:
        def __init__(self, auth):
            self.auth = auth

            self._amazon = None
            self._certificate = None
            self._generic = None
            self._password = None
            self._private_key = None
            self._upcred = None

        @property
        def amazon(self):
            self._amazon = self._amazon or AmazonCredential(self.auth)
            return self._amazon

        @property
        def certificate(self):
            self._certificate = self._certificate or CertificateCredential(self.auth)
            return self._certificate

        @property
        def generic(self):
            self._generic = self._generic or GenericCredential(self.auth)
            return self._generic

        @property
        def password(self):
            self._password = self._password or PasswordCredential(self.auth)
            return self._password

        @property
        def private_key(self):
            self._private_key = self._private_key or PrivateKeyCredential(self.auth)
            return self._private_key

        @property
        def username_password(self):
            self._upcred = self._upcred or UsernamePasswordCredential(self.auth)
            return self._upcred

    def __init__(self, auth):
        super().__init__(auth=auth)

        self._applications = None
        self._attributes = None
        self._ca = None
        self._certificate = None
        self._credentials = None
        self._device = None
        self._folder = None

    @property
    def application(self) -> _Applications:
        self._applications = self._applications or self._Applications(self.auth)
        return self._applications

    @property
    def attributes(self) -> Attributes:
        self._attributes = self._attributes or Attributes(self.auth)
        return self._attributes

    @property
    def certificate(self) -> Certificate:
        self._certificate = self._certificate or Certificate(self.auth)
        return self._certificate

    @property
    def certificate_authority(self) -> _CertificateAuthorities:
        self._ca = self._ca or self._CertificateAuthorities(self.auth)
        return self._ca

    @property
    def credential(self) -> _Credentials:
        self._credentials = self._credentials or self._Credentials(self.auth)
        return self._credentials

    @property
    def device(self) -> Device:
        self._device = self._device or Device(self.auth)
        return self._device

    @property
    def folder(self) -> Folder:
        self._folder = self._folder or Folder(self.auth)
        return self._folder


class AttributesNames:
    Application = ApplicationAttributes
    Certificate = CertificateAttributes
    CertificateAuthority = CertificateAuthorityAttributes
    Credentials = CredentialAttributes
    Device = DeviceAttributes
    Folder = FolderAttributes


class AttributeValues:
    Application = ApplicationAttributeValues


class Classes:
    Application = ApplicationClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    Device = DevicesClassNames
    Folder = FolderClassNames
