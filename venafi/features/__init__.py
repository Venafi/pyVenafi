from venafi.features.bases.feature_base import FeatureBase
from venafi.features.objects import Objects
from venafi.features.folder import Folder, FolderAttributes, FolderClassNames
from venafi.features.certificate import Certificate, CertificateAttributes, CertificateAttributeValues, CertificateClassNames
from venafi.features.device import Device, DeviceAttributes, DevicesClassNames
from venafi.features.application import A10AXTrafficManager, AmazonAWS, Apache, AzureKeyVault, Basic, BlueCoatSSLVA, CAPI, \
    CitrixNetScaler, ConnectDirect, F5AuthenticationBundle, F5LTMAdvanced, IBMDataPower, IBMGSK, ImpervaMX, JKS, JuniperSAS, \
    OracleIPlanet, PaloAltoNetworkFW, PEM, PKCS11, PKCS12, RiverbedSteelHead, TealeafPCA, VAMnShield, ApplicationAttributes, \
    ApplicationAttributeValues, ApplicationClassNames
from venafi.features.credentials import AmazonCredential, CertificateCredential, GenericCredential, \
    PasswordCredential, PrivateKeyCredential, UsernamePasswordCredential, CredentialAttributes
from venafi.features.certificate_authorities import AdaptableCA, MSCA, SelfSignedCA, CertificateAuthorityAttributes, \
    CertificateAuthorityClassNames


class Features:
    class _Applications:
        def __init__(self, auth):
            self._auth = auth

            self._a10_ax_traffic_manager = None
            self._amazon_aws = None
            self._apache = None
            self._azure_key_vault = None
            self._basic = None
            self._blue_coat_sslva = None
            self._capi = None
            self._citrix_net_scaler = None
            self._connect_direct = None
            self._f5_authentication_bundle = None
            self._f5_ltm_advanced = None
            self._ibm_datapower = None
            self._ibm_gsk = None
            self._imperva_mx = None
            self._jks = None
            self._juniper_sas = None
            self._oracle_iplanet = None
            self._palo_alto_network_fw = None
            self._pem = None
            self._pkcs11 = None
            self._pkcs12 = None
            self._riverbed_steel_head = None
            self._tealeaf_pca = None
            self._vamnshield = None

        @property
        def a10_ax_traffic_manager(self):
            self._a10_ax_traffic_manager = self._a10_ax_traffic_manager or A10AXTrafficManager(self._auth)
            return self._a10_ax_traffic_manager

        @property
        def amazon_aws(self):
            self._amazon_aws = self._amazon_aws or AmazonAWS(self._auth)
            return self._amazon_aws

        @property
        def apache(self):
            self._apache = self._apache or Apache(self._auth)
            return self._apache

        @property
        def azure_key_vault(self):
            self._azure_key_vault = self._azure_key_vault or AzureKeyVault(self._auth)
            return self._azure_key_vault

        @property
        def basic(self):
            self._basic = self._basic or Basic(self._auth)
            return self._basic

        @property
        def blue_coat_sslva(self):
            self._blue_coat_sslva = self._blue_coat_sslva or BlueCoatSSLVA(self._auth)
            return self._blue_coat_sslva

        @property
        def capi(self):
            self._capi = self._capi or CAPI(self._auth)
            return self._capi

        @property
        def citrix_net_scaler(self):
            self._citrix_net_scaler = self._citrix_net_scaler or CitrixNetScaler(self._auth)
            return self._citrix_net_scaler

        @property
        def connect_direct(self):
            self._connect_direct = self._connect_direct or ConnectDirect(self._auth)
            return self._connect_direct

        @property
        def f5_authentication_bundle(self):
            self._f5_authentication_bundle = self._f5_authentication_bundle or F5AuthenticationBundle(self._auth)
            return self._f5_authentication_bundle

        @property
        def f5_ltm_advanced(self):
            self._f5_ltm_advanced = self._f5_ltm_advanced or F5LTMAdvanced(self._auth)
            return self._f5_ltm_advanced

        @property
        def ibm_datapower(self):
            self._ibm_datapower = self._ibm_datapower or IBMDataPower(self._auth)
            return self._ibm_datapower

        @property
        def ibm_gsk(self):
            self._ibm_gsk = self._ibm_gsk or IBMGSK(self._auth)
            return self._ibm_gsk

        @property
        def imperva_mx(self):
            self._imperva_mx = self._imperva_mx or ImpervaMX(self._auth)
            return self._imperva_mx

        @property
        def jks(self):
            self._jks = self._jks or JKS(self._auth)
            return self._jks

        @property
        def juniper_sas(self):
            self._juniper_sas = self._juniper_sas or JuniperSAS(self._auth)
            return self._juniper_sas

        @property
        def oracle_iplanet(self):
            self._oracle_iplanet = self._oracle_iplanet or OracleIPlanet(self._auth)
            return self._oracle_iplanet

        @property
        def palo_alto_network_fw(self):
            self._palo_alto_network_fw = self._palo_alto_network_fw or PaloAltoNetworkFW(self._auth)
            return self._palo_alto_network_fw

        @property
        def pem(self):
            self._pem = self._pem or PEM(self._auth)
            return self._pem

        @property
        def pkcs11(self):
            self._pkcs11 = self._pkcs11 or PKCS11(self._auth)
            return self._pkcs11

        @property
        def pkcs12(self):
            self._pkcs12 = self._pkcs12 or PKCS12(self._auth)
            return self._pkcs12

        @property
        def riverbed_steel_head(self):
            self._riverbed_steel_head = self._riverbed_steel_head or RiverbedSteelHead(self._auth)
            return self._riverbed_steel_head

        @property
        def tealeaf_pca(self):
            self._tealeaf_pca = self._tealeaf_pca or TealeafPCA(self._auth)
            return self._tealeaf_pca

        @property
        def vamnshield(self):
            self._vamnshield = self._vamnshield or VAMnShield(self._auth)
            return self._vamnshield

    class _CertificateAuthorities:
        def __init__(self, auth):
            self._auth = auth

            self._adaptable = None
            self._msca = None
            self._self_signed = None

        @property
        def adaptable(self) -> AdaptableCA:
            self._adaptable = self._adaptable or AdaptableCA(self._auth)
            return self._adaptable

        @property
        def msca(self) -> MSCA:
            self._msca = self._msca or MSCA(self._auth)
            return self._msca

        @property
        def self_signed(self) -> SelfSignedCA:
            self._self_signed = self._self_signed or SelfSignedCA(self._auth)
            return self._self_signed

    class _Credentials:
        def __init__(self, auth):
            self._auth = auth

            self._amazon = None
            self._certificate = None
            self._generic = None
            self._password = None
            self._private_key = None
            self._upcred = None

        @property
        def amazon(self):
            self._amazon = self._amazon or AmazonCredential(self._auth)
            return self._amazon

        @property
        def certificate(self):
            self._certificate = self._certificate or CertificateCredential(self._auth)
            return self._certificate

        @property
        def generic(self):
            self._generic = self._generic or GenericCredential(self._auth)
            return self._generic

        @property
        def password(self):
            self._password = self._password or PasswordCredential(self._auth)
            return self._password

        @property
        def private_key(self):
            self._private_key = self._private_key or PrivateKeyCredential(self._auth)
            return self._private_key

        @property
        def username_password(self):
            self._upcred = self._upcred or UsernamePasswordCredential(self._auth)
            return self._upcred

    def __init__(self, auth):
        self._auth = auth
        
        self._applications = None
        self._objects = None
        self._ca = None
        self._certificate = None
        self._credentials = None
        self._device = None
        self._folder = None

    @property
    def application(self) -> _Applications:
        self._applications = self._applications or self._Applications(self._auth)
        return self._applications

    @property
    def objects(self) -> Objects:
        self._objects = self._objects or Objects(self._auth)
        return self._objects

    @property
    def certificate(self) -> Certificate:
        self._certificate = self._certificate or Certificate(self._auth)
        return self._certificate

    @property
    def certificate_authority(self) -> _CertificateAuthorities:
        self._ca = self._ca or self._CertificateAuthorities(self._auth)
        return self._ca

    @property
    def credential(self) -> _Credentials:
        self._credentials = self._credentials or self._Credentials(self._auth)
        return self._credentials

    @property
    def device(self) -> Device:
        self._device = self._device or Device(self._auth)
        return self._device

    @property
    def folder(self) -> Folder:
        self._folder = self._folder or Folder(self._auth)
        return self._folder


class AttributeNames:
    Application = ApplicationAttributes
    Certificate = CertificateAttributes
    CertificateAuthority = CertificateAuthorityAttributes
    Credentials = CredentialAttributes
    Device = DeviceAttributes
    Folder = FolderAttributes


class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues


class Classes:
    Application = ApplicationClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    Device = DevicesClassNames
    Folder = FolderClassNames
