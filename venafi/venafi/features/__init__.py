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
from venafi.features.identity import User, Group, IdentityClassNames, IdentityAttributes
from venafi.features.permissions import Permissions
from venafi.features.workflow import ReasonCode, AdaptableWorkflow, StandardWorkflow, Ticket, WorkflowAttributes, \
    WorkflowAttributeValues, WorkflowClassNames
from venafi.features.custom_fields import CustomField, CustomFieldAttributes, CustomFieldAttributeValues


# region Features
class _Application:
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
    def a10_ax_traffic_manager(self) -> A10AXTrafficManager:
        self._a10_ax_traffic_manager = self._a10_ax_traffic_manager or A10AXTrafficManager(self._auth)
        return self._a10_ax_traffic_manager

    @property
    def amazon_aws(self) -> AmazonAWS:
        self._amazon_aws = self._amazon_aws or AmazonAWS(self._auth)
        return self._amazon_aws

    @property
    def apache(self) -> Apache:
        self._apache = self._apache or Apache(self._auth)
        return self._apache

    @property
    def azure_key_vault(self) -> AzureKeyVault:
        self._azure_key_vault = self._azure_key_vault or AzureKeyVault(self._auth)
        return self._azure_key_vault

    @property
    def basic(self) -> Basic:
        self._basic = self._basic or Basic(self._auth)
        return self._basic

    @property
    def blue_coat_sslva(self) -> BlueCoatSSLVA:
        self._blue_coat_sslva = self._blue_coat_sslva or BlueCoatSSLVA(self._auth)
        return self._blue_coat_sslva

    @property
    def capi(self) -> CAPI:
        self._capi = self._capi or CAPI(self._auth)
        return self._capi

    @property
    def citrix_net_scaler(self) -> CitrixNetScaler:
        self._citrix_net_scaler = self._citrix_net_scaler or CitrixNetScaler(self._auth)
        return self._citrix_net_scaler

    @property
    def connect_direct(self) -> ConnectDirect:
        self._connect_direct = self._connect_direct or ConnectDirect(self._auth)
        return self._connect_direct

    @property
    def f5_authentication_bundle(self) -> F5AuthenticationBundle:
        self._f5_authentication_bundle = self._f5_authentication_bundle or F5AuthenticationBundle(self._auth)
        return self._f5_authentication_bundle

    @property
    def f5_ltm_advanced(self) -> F5LTMAdvanced:
        self._f5_ltm_advanced = self._f5_ltm_advanced or F5LTMAdvanced(self._auth)
        return self._f5_ltm_advanced

    @property
    def ibm_datapower(self) -> IBMDataPower:
        self._ibm_datapower = self._ibm_datapower or IBMDataPower(self._auth)
        return self._ibm_datapower

    @property
    def ibm_gsk(self) -> IBMGSK:
        self._ibm_gsk = self._ibm_gsk or IBMGSK(self._auth)
        return self._ibm_gsk

    @property
    def imperva_mx(self) -> ImpervaMX:
        self._imperva_mx = self._imperva_mx or ImpervaMX(self._auth)
        return self._imperva_mx

    @property
    def jks(self) -> JKS:
        self._jks = self._jks or JKS(self._auth)
        return self._jks

    @property
    def juniper_sas(self) -> JuniperSAS:
        self._juniper_sas = self._juniper_sas or JuniperSAS(self._auth)
        return self._juniper_sas

    @property
    def oracle_iplanet(self) -> OracleIPlanet:
        self._oracle_iplanet = self._oracle_iplanet or OracleIPlanet(self._auth)
        return self._oracle_iplanet

    @property
    def palo_alto_network_fw(self) -> PaloAltoNetworkFW:
        self._palo_alto_network_fw = self._palo_alto_network_fw or PaloAltoNetworkFW(self._auth)
        return self._palo_alto_network_fw

    @property
    def pem(self) -> PEM:
        self._pem = self._pem or PEM(self._auth)
        return self._pem

    @property
    def pkcs11(self) -> PKCS11:
        self._pkcs11 = self._pkcs11 or PKCS11(self._auth)
        return self._pkcs11

    @property
    def pkcs12(self) -> PKCS12:
        self._pkcs12 = self._pkcs12 or PKCS12(self._auth)
        return self._pkcs12

    @property
    def riverbed_steel_head(self) -> RiverbedSteelHead:
        self._riverbed_steel_head = self._riverbed_steel_head or RiverbedSteelHead(self._auth)
        return self._riverbed_steel_head

    @property
    def tealeaf_pca(self) -> TealeafPCA:
        self._tealeaf_pca = self._tealeaf_pca or TealeafPCA(self._auth)
        return self._tealeaf_pca

    @property
    def vamnshield(self) -> VAMnShield:
        self._vamnshield = self._vamnshield or VAMnShield(self._auth)
        return self._vamnshield


class _CertificateAuthority:
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


class _Credential:
    def __init__(self, auth):
        self._auth = auth

        self._amazon = None
        self._certificate = None
        self._generic = None
        self._password = None
        self._private_key = None
        self._upcred = None

    @property
    def amazon(self) -> AmazonCredential:
        self._amazon = self._amazon or AmazonCredential(self._auth)
        return self._amazon

    @property
    def certificate(self) -> CertificateCredential:
        self._certificate = self._certificate or CertificateCredential(self._auth)
        return self._certificate

    @property
    def generic(self) -> GenericCredential:
        self._generic = self._generic or GenericCredential(self._auth)
        return self._generic

    @property
    def password(self) -> PasswordCredential:
        self._password = self._password or PasswordCredential(self._auth)
        return self._password

    @property
    def private_key(self) -> PrivateKeyCredential:
        self._private_key = self._private_key or PrivateKeyCredential(self._auth)
        return self._private_key

    @property
    def username_password(self) -> UsernamePasswordCredential:
        self._upcred = self._upcred or UsernamePasswordCredential(self._auth)
        return self._upcred


class _Identity:
    def __init__(self, auth):
        self._auth = auth

        self._group = None
        self._user = None

    @property
    def group(self) -> Group:
        self._group = self._group or Group(self._auth)
        return self._group

    @property
    def user(self) -> User:
        self._user = self._user or User(self._auth)
        return self._user


class _Workflow:
    def __init__(self, auth):
        self._auth = auth

        self._adaptable = None
        self._reason_code = None
        self._standard = None
        self._ticket = None

    @property
    def adaptable(self) -> AdaptableWorkflow:
        self._adaptable = self._adaptable or AdaptableWorkflow(self._auth)
        return self._adaptable

    @property
    def reason_code(self) -> ReasonCode:
        self._reason_code = self._reason_code or ReasonCode(self._auth)
        return self._reason_code

    @property
    def standard(self) -> StandardWorkflow:
        self._standard = self._standard or StandardWorkflow(self._auth)
        return self._standard

    @property
    def ticket(self) -> Ticket:
        self._ticket = self._ticket or Ticket(self._auth)
        return self._ticket


class Features:
    def __init__(self, auth):
        self._auth = auth
        
        self._applications = None
        self._objects = None
        self._ca = None
        self._certificate = None
        self._credentials = None
        self._custom_fields = None
        self._device = None
        self._folder = None
        self._identity = None
        self._permissions = None
        self._workflow = None

    @property
    def application(self) -> _Application:
        self._applications = self._applications or _Application(self._auth)
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
    def certificate_authority(self) -> _CertificateAuthority:
        self._ca = self._ca or _CertificateAuthority(self._auth)
        return self._ca

    @property
    def credential(self) -> _Credential:
        self._credentials = self._credentials or _Credential(self._auth)
        return self._credentials

    @property
    def custom_fields(self) -> CustomField:
        self._custom_fields = self._custom_fields or CustomField(self._auth)
        return self._custom_fields

    @property
    def device(self) -> Device:
        self._device = self._device or Device(self._auth)
        return self._device

    @property
    def folder(self) -> Folder:
        self._folder = self._folder or Folder(self._auth)
        return self._folder

    @property
    def identity(self) -> _Identity:
        self._identity = self._identity or _Identity(self._auth)
        return self._identity

    @property
    def permissions(self) -> Permissions:
        self._permissions = self._permissions or Permissions(self._auth)
        return self._permissions

    @property
    def workflow(self) -> _Workflow:
        self._workflow = self._workflow or _Workflow(self._auth)
        return self._workflow

# endregion


# region AttributeNames, AttributeValues, and Classes
class AttributeNames:
    Application = ApplicationAttributes
    Certificate = CertificateAttributes
    CertificateAuthority = CertificateAuthorityAttributes
    Credentials = CredentialAttributes
    CustomField = CustomFieldAttributes
    Device = DeviceAttributes
    Folder = FolderAttributes
    Identity = IdentityAttributes
    Workflow = WorkflowAttributes


class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues
    CustomField = CustomFieldAttributeValues
    Workflow = WorkflowAttributeValues


class Classes:
    Application = ApplicationClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    Device = DevicesClassNames
    Folder = FolderClassNames
    Identity = IdentityClassNames
    Workflow = WorkflowClassNames

# endregion
