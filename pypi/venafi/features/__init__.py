from venafi.features.folder import Folder, FolderAttributes
from venafi.features.certificate import Certificate, CertificateAttributes
from venafi.features.device import Device, DeviceAttributes
from venafi.features.application import Apache, PKCS11, ApplicationAttributes, ApplicationAttributeValues
from venafi.features.credentials import UsernamePasswordCredential, CredentialAttributes
from venafi.features.certificate_authorities import MSCA, SelfSigned, CertificateAuthorityAttributes


class Features:
    def __init__(self, auth):
        self.auth = auth

        self._applications = None
        self._ca = None
        self._certificate = None
        self._credentials = None
        self._device = None
        self._folder = None

    @property
    def application(self):
        self._applications = self._applications or self._Applications(self.auth)
        return self._applications

    @property
    def certificate(self):
        self._certificate = self._certificate or Certificate(self.auth)
        return self._certificate

    @property
    def certificate_authority(self):
        self._ca = self._ca or self._CertificateAuthorities(self.auth)
        return self._ca

    @property
    def credential(self):
        self._credentials = self._credentials or self._Credentials(self.auth)
        return self._credentials

    @property
    def device(self):
        self._device = self._device or Device(self.auth)
        return self._device

    @property
    def folder(self):
        self._folder = self._folder or Folder(self.auth)
        return self._folder

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

            self._upcred = None

        @property
        def username_password(self):
            self._upcred = self._upcred or UsernamePasswordCredential(self.auth)
            return self._upcred


class Attributes:
    Application = ApplicationAttributes
    Certificate = CertificateAttributes
    CertificateAuthority = CertificateAuthorityAttributes
    Credentials = CredentialAttributes
    Device = DeviceAttributes
    Folder = FolderAttributes


class AttributeValues:
    Application = ApplicationAttributeValues
