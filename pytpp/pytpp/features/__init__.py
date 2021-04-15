from pytpp.features.bases.feature_base import FeatureBase
from pytpp.features.objects import Objects
from pytpp.features.folder import Folder, FolderAttributes, FolderClassNames
from pytpp.features.certificate import Certificate, CertificateAttributes, CertificateAttributeValues, CertificateClassNames
from pytpp.features.device import Device, DeviceAttributes, DevicesClassNames, DeviceAttributeValues
from pytpp.features.application import A10AXTrafficManager, AmazonAWS, Apache, AzureKeyVault, Basic, BlueCoatSSLVA, CAPI, \
    CitrixNetScaler, ConnectDirect, F5AuthenticationBundle, F5LTMAdvanced, IBMDataPower, IBMGSK, ImpervaMX, JKS, JuniperSAS, \
    OracleIPlanet, PaloAltoNetworkFW, PEM, PKCS11, PKCS12, RiverbedSteelHead, TealeafPCA, VAMnShield, ApplicationAttributes, \
    ApplicationAttributeValues, ApplicationClassNames
from pytpp.features.discovery import NetworkDiscovery, DiscoveryClassNames, DiscoveryAttributeValues, DiscoveryAttributes
from pytpp.features.credentials import AmazonCredential, CertificateCredential, GenericCredential, \
    PasswordCredential, PrivateKeyCredential, UsernamePasswordCredential, CredentialAttributes
from pytpp.features.certificate_authorities import AdaptableCA, MSCA, SelfSignedCA, CertificateAuthorityAttributes, \
    CertificateAuthorityClassNames
from pytpp.features.identity import User, Group, IdentityClassNames, IdentityAttributes
from pytpp.features.permissions import Permissions
from pytpp.features.platform import AutoLayoutManager, BulkProvisioningManager, CAImportManager, CertificateManager,\
    CertificatePreEnrollment, CertificateRevocation, CloudInstanceMonitor, DiscoveryManager, Monitor, \
    OnboardDiscoveryManager, Reporting, SSHManager, TrustNetManager, ValidationManager, PlatformsAttributes, \
    PlatformsClassNames
from pytpp.features.placement_rules import PlacementRules, PlacementRulesAttributeNames, PlacementRulesAttributeValues, \
    PlacementRulesClassNames, PlacementRuleCondition
from pytpp.features.workflow import ReasonCode, AdaptableWorkflow, StandardWorkflow, Ticket, WorkflowAttributes, \
    WorkflowAttributeValues, WorkflowClassNames
from pytpp.features.custom_fields import CustomField, CustomFieldAttributes, CustomFieldAttributeValues


# region Features
class _Application:
    def __init__(self, api):
        self._api = api

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
        self._a10_ax_traffic_manager = self._a10_ax_traffic_manager or A10AXTrafficManager(self._api)
        return self._a10_ax_traffic_manager

    @property
    def amazon_aws(self) -> AmazonAWS:
        self._amazon_aws = self._amazon_aws or AmazonAWS(self._api)
        return self._amazon_aws

    @property
    def apache(self) -> Apache:
        self._apache = self._apache or Apache(self._api)
        return self._apache

    @property
    def azure_key_vault(self) -> AzureKeyVault:
        self._azure_key_vault = self._azure_key_vault or AzureKeyVault(self._api)
        return self._azure_key_vault

    @property
    def basic(self) -> Basic:
        self._basic = self._basic or Basic(self._api)
        return self._basic

    @property
    def blue_coat_sslva(self) -> BlueCoatSSLVA:
        self._blue_coat_sslva = self._blue_coat_sslva or BlueCoatSSLVA(self._api)
        return self._blue_coat_sslva

    @property
    def capi(self) -> CAPI:
        self._capi = self._capi or CAPI(self._api)
        return self._capi

    @property
    def citrix_net_scaler(self) -> CitrixNetScaler:
        self._citrix_net_scaler = self._citrix_net_scaler or CitrixNetScaler(self._api)
        return self._citrix_net_scaler

    @property
    def connect_direct(self) -> ConnectDirect:
        self._connect_direct = self._connect_direct or ConnectDirect(self._api)
        return self._connect_direct

    @property
    def f5_authentication_bundle(self) -> F5AuthenticationBundle:
        self._f5_authentication_bundle = self._f5_authentication_bundle or F5AuthenticationBundle(self._api)
        return self._f5_authentication_bundle

    @property
    def f5_ltm_advanced(self) -> F5LTMAdvanced:
        self._f5_ltm_advanced = self._f5_ltm_advanced or F5LTMAdvanced(self._api)
        return self._f5_ltm_advanced

    @property
    def ibm_datapower(self) -> IBMDataPower:
        self._ibm_datapower = self._ibm_datapower or IBMDataPower(self._api)
        return self._ibm_datapower

    @property
    def ibm_gsk(self) -> IBMGSK:
        self._ibm_gsk = self._ibm_gsk or IBMGSK(self._api)
        return self._ibm_gsk

    @property
    def imperva_mx(self) -> ImpervaMX:
        self._imperva_mx = self._imperva_mx or ImpervaMX(self._api)
        return self._imperva_mx

    @property
    def jks(self) -> JKS:
        self._jks = self._jks or JKS(self._api)
        return self._jks

    @property
    def juniper_sas(self) -> JuniperSAS:
        self._juniper_sas = self._juniper_sas or JuniperSAS(self._api)
        return self._juniper_sas

    @property
    def oracle_iplanet(self) -> OracleIPlanet:
        self._oracle_iplanet = self._oracle_iplanet or OracleIPlanet(self._api)
        return self._oracle_iplanet

    @property
    def palo_alto_network_fw(self) -> PaloAltoNetworkFW:
        self._palo_alto_network_fw = self._palo_alto_network_fw or PaloAltoNetworkFW(self._api)
        return self._palo_alto_network_fw

    @property
    def pem(self) -> PEM:
        self._pem = self._pem or PEM(self._api)
        return self._pem

    @property
    def pkcs11(self) -> PKCS11:
        self._pkcs11 = self._pkcs11 or PKCS11(self._api)
        return self._pkcs11

    @property
    def pkcs12(self) -> PKCS12:
        self._pkcs12 = self._pkcs12 or PKCS12(self._api)
        return self._pkcs12

    @property
    def riverbed_steel_head(self) -> RiverbedSteelHead:
        self._riverbed_steel_head = self._riverbed_steel_head or RiverbedSteelHead(self._api)
        return self._riverbed_steel_head

    @property
    def tealeaf_pca(self) -> TealeafPCA:
        self._tealeaf_pca = self._tealeaf_pca or TealeafPCA(self._api)
        return self._tealeaf_pca

    @property
    def vamnshield(self) -> VAMnShield:
        self._vamnshield = self._vamnshield or VAMnShield(self._api)
        return self._vamnshield


class _CertificateAuthority:
    def __init__(self, api):
        self._api = api

        self._adaptable = None
        self._msca = None
        self._self_signed = None

    @property
    def adaptable(self) -> AdaptableCA:
        self._adaptable = self._adaptable or AdaptableCA(self._api)
        return self._adaptable

    @property
    def msca(self) -> MSCA:
        self._msca = self._msca or MSCA(self._api)
        return self._msca

    @property
    def self_signed(self) -> SelfSignedCA:
        self._self_signed = self._self_signed or SelfSignedCA(self._api)
        return self._self_signed


class _Credential:
    def __init__(self, api):
        self._api = api

        self._amazon = None
        self._certificate = None
        self._generic = None
        self._password = None
        self._private_key = None
        self._upcred = None

    @property
    def amazon(self) -> AmazonCredential:
        self._amazon = self._amazon or AmazonCredential(self._api)
        return self._amazon

    @property
    def certificate(self) -> CertificateCredential:
        self._certificate = self._certificate or CertificateCredential(self._api)
        return self._certificate

    @property
    def generic(self) -> GenericCredential:
        self._generic = self._generic or GenericCredential(self._api)
        return self._generic

    @property
    def password(self) -> PasswordCredential:
        self._password = self._password or PasswordCredential(self._api)
        return self._password

    @property
    def private_key(self) -> PrivateKeyCredential:
        self._private_key = self._private_key or PrivateKeyCredential(self._api)
        return self._private_key

    @property
    def username_password(self) -> UsernamePasswordCredential:
        self._upcred = self._upcred or UsernamePasswordCredential(self._api)
        return self._upcred


class _Discovery:
    def __init__(self, api):
        self._api = api

        self._network = None

    @property
    def network(self) -> NetworkDiscovery:
        self._network = self._network or NetworkDiscovery(api=self._api)
        return self._network


class _Identity:
    def __init__(self, api):
        self._api = api

        self._group = None
        self._user = None

    @property
    def group(self) -> Group:
        self._group = self._group or Group(self._api)
        return self._group

    @property
    def user(self) -> User:
        self._user = self._user or User(self._api)
        return self._user


class _Platforms:
    def __init__(self, api):
        self._api = api

        self._auto_layout_manager = None
        self._bulk_provisioning_manager = None
        self._ca_import_manager = None
        self._certificate_manager = None
        self._certificate_pre_enrollment = None
        self._certificate_revocation = None
        self._cloud_instance_monitor = None
        self._discovery_manager = None
        self._monitor = None
        self._onboard_discovery_manager = None
        self._reporting = None
        self._ssh_manager = None
        self._trustnet_manager = None
        self._validation_manager = None

    @property
    def auto_layout_manager(self) -> AutoLayoutManager:
        self._auto_layout_manager = self._auto_layout_manager or AutoLayoutManager(self._api)
        return self._auto_layout_manager

    @property
    def bulk_provisioning_manager(self) -> BulkProvisioningManager:
        self._bulk_provisioning_manager = self._bulk_provisioning_manager or BulkProvisioningManager(self._api)
        return self._bulk_provisioning_manager

    @property
    def ca_import_manager(self) -> CAImportManager:
        self._ca_import_manager = self._ca_import_manager or CAImportManager(self._api)
        return self._ca_import_manager

    @property
    def certificate_manager(self) -> CertificateManager:
        self._certificate_manager = self._certificate_manager or CertificateManager(self._api)
        return self._certificate_manager

    @property
    def certificate_pre_enrollment(self) -> CertificatePreEnrollment:
        self._certificate_pre_enrollment = self._certificate_pre_enrollment or CertificatePreEnrollment(self._api)
        return self._certificate_pre_enrollment

    @property
    def certificate_revocation(self) -> CertificateRevocation:
        self._certificate_revocation = self._certificate_revocation or CertificateRevocation(self._api)
        return self._certificate_revocation

    @property
    def cloud_instance_monitor(self) -> CloudInstanceMonitor:
        self._cloud_instance_monitor = self._cloud_instance_monitor or CloudInstanceMonitor(self._api)
        return self._cloud_instance_monitor

    @property
    def discovery_manager(self) -> DiscoveryManager:
        self._discovery_manager = self._discovery_manager or DiscoveryManager(self._api)
        return self._discovery_manager

    @property
    def monitor(self) -> Monitor:
        self._monitor = self._monitor or Monitor(self._api)
        return self._monitor

    @property
    def onboard_discovery_manager(self) -> OnboardDiscoveryManager:
        self._onboard_discovery_manager = self._onboard_discovery_manager or OnboardDiscoveryManager(self._api)
        return self._onboard_discovery_manager

    @property
    def reporting(self) -> Reporting:
        self._reporting = self._reporting or Reporting(self._api)
        return self._reporting

    @property
    def ssh_manager(self) -> SSHManager:
        self._ssh_manager = self._ssh_manager or SSHManager(self._api)
        return self._ssh_manager

    @property
    def trustnet_manager(self) -> TrustNetManager:
        self._trustnet_manager = self._trustnet_manager or TrustNetManager(self._api)
        return self._trustnet_manager

    @property
    def validation_manager(self) -> ValidationManager:
        self._validation_manager = self._validation_manager or ValidationManager(self._api)
        return self._validation_manager


class _Workflow:
    def __init__(self, api):
        self._api = api

        self._adaptable = None
        self._reason_code = None
        self._standard = None
        self._ticket = None

    @property
    def adaptable(self) -> AdaptableWorkflow:
        self._adaptable = self._adaptable or AdaptableWorkflow(self._api)
        return self._adaptable

    @property
    def reason_code(self) -> ReasonCode:
        self._reason_code = self._reason_code or ReasonCode(self._api)
        return self._reason_code

    @property
    def standard(self) -> StandardWorkflow:
        self._standard = self._standard or StandardWorkflow(self._api)
        return self._standard

    @property
    def ticket(self) -> Ticket:
        self._ticket = self._ticket or Ticket(self._api)
        return self._ticket


class Features:
    def __init__(self, api):
        self._api = api
        
        self._applications = None
        self._objects = None
        self._ca = None
        self._certificate = None
        self._credentials = None
        self._custom_fields = None
        self._device = None
        self._discovery = None
        self._folder = None
        self._identity = None
        self._permissions = None
        self._placement_rule_condition = None
        self._placement_rules = None
        self._platforms = None
        self._workflow = None

    @property
    def application(self) -> _Application:
        self._applications = self._applications or _Application(self._api)
        return self._applications

    @property
    def objects(self) -> Objects:
        self._objects = self._objects or Objects(self._api)
        return self._objects

    @property
    def certificate(self) -> Certificate:
        self._certificate = self._certificate or Certificate(self._api)
        return self._certificate

    @property
    def certificate_authority(self) -> _CertificateAuthority:
        self._ca = self._ca or _CertificateAuthority(self._api)
        return self._ca

    @property
    def credential(self) -> _Credential:
        self._credentials = self._credentials or _Credential(self._api)
        return self._credentials

    @property
    def custom_fields(self) -> CustomField:
        self._custom_fields = self._custom_fields or CustomField(self._api)
        return self._custom_fields

    @property
    def device(self) -> Device:
        self._device = self._device or Device(self._api)
        return self._device

    @property
    def discovery(self) -> _Discovery:
        self._discovery = self._discovery or _Discovery(self._api)
        return self._discovery

    @property
    def folder(self) -> Folder:
        self._folder = self._folder or Folder(self._api)
        return self._folder

    @property
    def identity(self) -> _Identity:
        self._identity = self._identity or _Identity(self._api)
        return self._identity

    @property
    def permissions(self) -> Permissions:
        self._permissions = self._permissions or Permissions(self._api)
        return self._permissions

    @property
    def placement_rule_condition(self) -> PlacementRuleCondition:
        self._placement_rule_condition = self._placement_rule_condition or PlacementRuleCondition()
        return self._placement_rule_condition

    @property
    def placement_rules(self) -> PlacementRules:
        self._placement_rules = self._placement_rules or PlacementRules(self._api)
        return self._placement_rules

    @property
    def platforms(self) -> _Platforms:
        self._platforms = self._platforms or _Platforms(self._api)
        return self._platforms

    @property
    def workflow(self) -> _Workflow:
        self._workflow = self._workflow or _Workflow(self._api)
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
    Discovery = DiscoveryAttributes
    Folder = FolderAttributes
    Identity = IdentityAttributes
    PlacementRules = PlacementRulesAttributeNames
    Platforms = PlatformsAttributes
    Workflow = WorkflowAttributes


class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues
    CustomField = CustomFieldAttributeValues
    Device = DeviceAttributeValues
    Discovery = DiscoveryAttributeValues
    PlacementRules = PlacementRulesAttributeValues
    Workflow = WorkflowAttributeValues


class Classes:
    Application = ApplicationClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    Device = DevicesClassNames
    Discovery = DiscoveryClassNames
    Folder = FolderClassNames
    Identity = IdentityClassNames
    PlacementRules = PlacementRulesClassNames
    Platforms = PlatformsClassNames
    Workflow = WorkflowClassNames

# endregion
