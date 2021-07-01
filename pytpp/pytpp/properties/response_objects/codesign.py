from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string
from typing import List


class CodeSign:
    class ResultCode:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.codesign_result = ResultCodes.CodeSign.get(code, 'Unknown')

    class Items:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.items = response_object.get('Items')  # type: List[str]

    class InfoValue:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.info = response_object.get('Info')  # type: int
            self.value = CodeSign.Items(response_object.get('Value'))

    class RightsKeyValue:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key = response_object.get('key')  # type: str
            self.value = response_object.get('value')  # type: int

    class CertificateTemplate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allow_user_key_import = response_object.get('AllowUserKeyImport')  # type: bool
            self.certificate_authority_dn = CodeSign.InfoValue(response_object.get('CertificateAuthorityDN'))
            self.certificate_subject = response_object.get('CertificateSubject')  # type: str
            self.city = CodeSign.InfoValue(response_object.get('City'))
            self.country = CodeSign.InfoValue(response_object.get('Country'))
            self.dn = response_object.get('Dn')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.key_algorithm = CodeSign.InfoValue(response_object.get('KeyAlgorithm'))
            self.key_storage_location = CodeSign.InfoValue(response_object.get('KeyStorageLocation'))
            self.key_use_flow_dn = response_object.get('KeyUseFlowDN')  # type: str
            self.object_naming_pattern = response_object.get('ObjectNamingPattern')  # type: str
            self.organization = CodeSign.InfoValue(response_object.get('Organization'))
            self.organizational_unit = CodeSign.InfoValue(response_object.get('OrganizationalUnit'))
            self.per_user = response_object.get('PerUser')  # type: bool
            self.san_email = CodeSign.InfoValue(response_object.get('SANEmail'))
            self.state = CodeSign.InfoValue(response_object.get('State'))
            self.target_policy_dn = response_object.get('TargetPolicyDN')  # type: str
            self.type = response_object.get('Type')  # type: str
            self.visible_to = CodeSign.Items(response_object.get('VisibleTo'))

    class CertificateEnvironment:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allow_user_key_import = response_object.get('AllowUserKeyImport')  # type: bool
            self.certificate_authority_dn = CodeSign.InfoValue(response_object.get('CertificateAuthorityDN'))
            self.certificate_dn = response_object.get('CertificateDN')  # type: str
            self.certificate_stage = response_object.get('CertificateStage')  # type: int
            self.certificate_status_text = response_object.get('CertificateStatusText')  # type: str
            self.certificate_subject = response_object.get('CertificateSubject')  # type: str
            self.certificate_template = CodeSign.CertificateTemplate(response_object.get('CertificateTemplate'))
            self.city = CodeSign.InfoValue(response_object.get('City'))
            self.country = CodeSign.InfoValue(response_object.get('Country'))
            self.dn = response_object.get('Dn')  # type: str
            self.grouping = response_object.get('Grouping')  # type: int
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.ip_address_restriction = CodeSign.Items(response_object.get('IPAddressRestriction'))
            self.key_algorithm = CodeSign.InfoValue(response_object.get('KeyAlgorithm'))
            self.key_storage_location = CodeSign.InfoValue(response_object.get('KeyStorageLocation'))
            self.key_use_flow_dn = response_object.get('KeyUseFlowDN')  # type: str
            self.object_naming_pattern = response_object.get('ObjectNamingPattern')  # type: str
            self.organization = CodeSign.InfoValue(response_object.get('Organization'))
            self.organizational_unit = CodeSign.InfoValue(response_object.get('OrganizationalUnit'))
            self.per_user = response_object.get('PerUser')  # type: bool
            self.read_only = response_object.get('ReadOnly')  # type: bool
            self.san_email = CodeSign.InfoValue(response_object.get('SANEmail'))
            self.state = CodeSign.InfoValue(response_object.get('State'))
            self.target_policy_dn = response_object.get('TargetPolicyDN')  # type: str
            self.template_dn = response_object.get('TemplateDN')  # type: str
            self.type = response_object.get('Type')  # type: str
            self.visible_to = CodeSign.Items(response_object.get('VisibleTo'))

    class KeyStorageLocations:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.items = response_object.get('Items')  # type: List[str]

    class Application:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.dn = response_object.get('Dn')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int

    class ApplicationCollection:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.application_dns = CodeSign.Items(response_object.get('ApplicationDNs'))
            self.dn = response_object.get('Dn')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int

    class CSPTemplate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allow_user_key_import = response_object.get('AllowUserKeyImport')  # type: bool
            self.dn = response_object.get('Dn')  # type: str
            self.encryption_key_algorithm = CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm'))
            self.expiration = CodeSign.InfoValue(response_object.get('Expiration'))
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.key_storage_location = CodeSign.InfoValue(response_object.get('KeyStorageLocation'))
            self.max_uses = CodeSign.InfoValue(response_object.get('MaxUses'))
            self.signing_key_algorithm = CodeSign.InfoValue(response_object.get('SigningKeyAlgorithm'))
            self.type = response_object.get('Type')  # type: str
            self.visible_to = CodeSign.Items(response_object.get('VisibleTo'))

    class DotNetTemplate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allow_user_key_import = response_object.get('AllowUserKeyImport')  # type: bool
            self.description = response_object.get('Description')  # type: str
            self.dn = response_object.get('Dn')  # type: str
            self.encryption_key_algorithm = CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm'))
            self.expiration = CodeSign.InfoValue(response_object.get('Expiration'))
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.key_algorithm = CodeSign.InfoValue(response_object.get('KeyAlgorithm'))
            self.key_container_dn = CodeSign.InfoValue(response_object.get('KeyContainerDN'))
            self.key_storage_location = CodeSign.InfoValue(response_object.get('KeyStorageLocation'))
            self.key_use_flow_dn = response_object.get('KeyUseFlowDN')  # type: str
            self.max_uses = CodeSign.InfoValue(response_object.get('MaxUses'))
            self.type = response_object.get('Type')  # type: str
            self.visible_to = CodeSign.Items(response_object.get('VisibleTo'))

    class GPGTemplate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allow_user_key_import = response_object.get('AllowUserKeyImport')  # type: bool
            self.authentication_key_algorithm = CodeSign.InfoValue(response_object.get('AuthenticationKeyAlgorithm'))
            self.dn = response_object.get('Dn')  # type: str
            self.email = CodeSign.InfoValue(response_object.get('Email'))
            self.encryption_key_algorithm = CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm'))
            self.expiration = CodeSign.InfoValue(response_object.get('Expiration'))
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.key_storage_location = CodeSign.InfoValue(response_object.get('KeyStorageLocation'))
            self.key_use_flow_dn = response_object.get('KeyUseFlowDN')  # type: str
            self.max_uses = CodeSign.InfoValue(response_object.get('MaxUses'))
            self.object_naming_pattern = response_object.get('ObjectNamingPattern')  # type: str
            self.per_user = response_object.get('PerUser')  # type: bool
            self.real_name = CodeSign.InfoValue(response_object.get('RealName'))
            self.signing_key_algorithm = CodeSign.InfoValue(response_object.get('SigningKeyAlgorithm'))
            self.type = response_object.get('Type')  # type: str
            self.visible_to = CodeSign.Items(response_object.get('VisibleTo'))

    class GlobalConfiguration:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.approved_key_storage_locations = CodeSign.KeyStorageLocations(
                response_object.get('ApprovedKeyStorageLocations')
            )
            self.available_key_storage_locations = CodeSign.KeyStorageLocations(
                response_object.get('AvailableKeyStorageLocations')
            )
            self.default_ca_container = response_object.get('DefaultCAContainer')  # type: str
            self.default_certificate_container = response_object.get('DefaultCertificateContainer')  # type: str
            self.default_credential_container = response_object.get('DefaultCredentialContainer')  # type: str
            self.key_use_timeout = response_object.get('KeyUseTimeout')  # type: int
            self.project_description_tooltip = response_object.get('ProjectDescriptionTooltip')  # type: str
            self.request_in_progress_message = response_object.get('RequestInProgressMessage')  # type: str

    class Project:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            
            self.application_dns = CodeSign.Items(response_object.get('ApplicationDNs'))
            self.applications = [CodeSign.Application(a) for a in response_object.get('Applications')]
            self.auditors = CodeSign.Items(response_object.get('Auditors'))
            self.certificate_environments = [
                CodeSign.CertificateEnvironment(ce)
                for ce in response_object.get('CertificateEnvironments')
            ]
            self.collections = [
                CodeSign.SignApplicationCollection(c)
                for c in response_object.get('Collections')
            ]
            self.created_on = from_date_string(response_object.get('CreatedOn'))
            self.description = response_object.get('Description')  # type: str
            self.dn = response_object.get('Dn')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.key_use_approvers = CodeSign.Items(response_object.get('KeyUseApprovers'))
            self.key_users = CodeSign.Items(response_object.get('KeyUsers'))
            self.owners = CodeSign.Items(response_object.get('Owners'))
            self.status = response_object.get('Status')  # type: int

    class Rights:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.rights = response_object.get('Rights')  # type: int
            self.none = self.rights == 0
            self.admin = self.rights&1 != 0
            self.use = self.rights&2 != 0
            self.audit = self.rights&4 != 0
            self.owner = self.rights&8 != 0
            self.project_approval = self.rights&16 != 0
            self.application_admin = self.rights&32 != 0
            self.approve_use = self.rights&64 != 0

    class SignApplicationCollection:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.description = response_object.get('Description')  # type: str
            self.dn = response_object.get('Dn')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.hash = response_object.get('Hash')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.location = response_object.get('Location')  # type: str
            self.permitted_argument_pattern = response_object.get('PermittedArgumentPattern')  # type: str
            self.signatory_issuer = response_object.get('SignatoryIssuer')  # type: str
            self.signatory_subject = response_object.get('SignatorySubject')  # type: str
            self.size = response_object.get('Size')  # type: int
            self.version = response_object.get('Version')  # type: str
