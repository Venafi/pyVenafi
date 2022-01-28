from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.properties.response_objects.dataclasses import codesign


class CodeSign:
    @staticmethod
    def ResultCode(code: int):
        return codesign.ResultCode(
            code=code,
            codesign_result=ResultCodes.CodeSign.get(code, 'Unknown'),
        )

    @staticmethod
    def Items(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.Items(
            items=response_object.get('Items'),
        )

    @staticmethod
    def InfoValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.InfoValue(
            info=response_object.get('Info'),
            value=CodeSign.Items(response_object.get('Value')),
        )

    @staticmethod
    def RightsKeyValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.RightsKeyValue(
            key=response_object.get('key'),
            value=response_object.get('value'),
        )

    @staticmethod
    def CertificateTemplate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.CertificateTemplate(
            allow_user_key_import=response_object.get('AllowUserKeyImport'),
            certificate_authority_dn=CodeSign.InfoValue(response_object.get('CertificateAuthorityDN')),
            certificate_subject=response_object.get('CertificateSubject'),
            city=CodeSign.InfoValue(response_object.get('City')),
            country=CodeSign.InfoValue(response_object.get('Country')),
            dn=response_object.get('Dn'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            key_algorithm=CodeSign.InfoValue(response_object.get('KeyAlgorithm')),
            key_storage_location=CodeSign.InfoValue(response_object.get('KeyStorageLocation')),
            key_use_flow_dn=response_object.get('KeyUseFlowDN'),
            object_naming_pattern=response_object.get('ObjectNamingPattern'),
            organization=CodeSign.InfoValue(response_object.get('Organization')),
            organizational_unit=CodeSign.InfoValue(response_object.get('OrganizationalUnit')),
            per_user=response_object.get('PerUser'),
            san_email=CodeSign.InfoValue(response_object.get('SANEmail')),
            state=CodeSign.InfoValue(response_object.get('State')),
            target_policy_dn=response_object.get('TargetPolicyDN'),
            type=response_object.get('Type'),
            visible_to=CodeSign.Items(response_object.get('VisibleTo')),
        )

    @staticmethod
    def CertificateEnvironment(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.CertificateEnvironment(
            allow_user_key_import=response_object.get('AllowUserKeyImport'),
            certificate_authority_dn=CodeSign.InfoValue(response_object.get('CertificateAuthorityDN')),
            certificate_dn=response_object.get('CertificateDN'),
            certificate_stage=response_object.get('CertificateStage'),
            certificate_status_text=response_object.get('CertificateStatusText'),
            certificate_subject=response_object.get('CertificateSubject'),
            certificate_template=CodeSign.CertificateTemplate(response_object.get('CertificateTemplate')),
            city=CodeSign.InfoValue(response_object.get('City')),
            country=CodeSign.InfoValue(response_object.get('Country')),
            dn=response_object.get('Dn'),
            grouping=response_object.get('Grouping'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            ip_address_restriction=CodeSign.Items(response_object.get('IPAddressRestriction')),
            key_algorithm=CodeSign.InfoValue(response_object.get('KeyAlgorithm')),
            key_storage_location=CodeSign.InfoValue(response_object.get('KeyStorageLocation')),
            key_use_flow_dn=response_object.get('KeyUseFlowDN'),
            object_naming_pattern=response_object.get('ObjectNamingPattern'),
            organization=CodeSign.InfoValue(response_object.get('Organization')),
            organizational_unit=CodeSign.InfoValue(response_object.get('OrganizationalUnit')),
            per_user=response_object.get('PerUser'),
            read_only=response_object.get('ReadOnly'),
            san_email=CodeSign.InfoValue(response_object.get('SANEmail')),
            state=CodeSign.InfoValue(response_object.get('State')),
            target_policy_dn=response_object.get('TargetPolicyDN'),
            template_dn=response_object.get('TemplateDN'),
            type=response_object.get('Type'),
            visible_to=CodeSign.Items(response_object.get('VisibleTo')),
        )

    @staticmethod
    def KeyStorageLocations(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.KeyStorageLocations(
            items=response_object.get('Items'),
        )

    @staticmethod
    def Application(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.Application(
            dn=response_object.get('Dn'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
        )

    @staticmethod
    def ApplicationCollection(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.ApplicationCollection(
            application_dns=CodeSign.Items(response_object.get('ApplicationDNs')),
            dn=response_object.get('Dn'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
        )

    @staticmethod
    def CSPTemplate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.CSPTemplate(
            allow_user_key_import=response_object.get('AllowUserKeyImport'),
            dn=response_object.get('Dn'),
            encryption_key_algorithm=CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm')),
            expiration=CodeSign.InfoValue(response_object.get('Expiration')),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            key_storage_location=CodeSign.InfoValue(response_object.get('KeyStorageLocation')),
            max_uses=CodeSign.InfoValue(response_object.get('MaxUses')),
            signing_key_algorithm=CodeSign.InfoValue(response_object.get('SigningKeyAlgorithm')),
            type=response_object.get('Type'),
            visible_to=CodeSign.Items(response_object.get('VisibleTo')),
        )

    @staticmethod
    def DotNetTemplate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.DotNetTemplate(
            allow_user_key_import=response_object.get('AllowUserKeyImport'),
            description=response_object.get('Description'),
            dn=response_object.get('Dn'),
            encryption_key_algorithm=CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm')),
            expiration=CodeSign.InfoValue(response_object.get('Expiration')),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            key_algorithm=CodeSign.InfoValue(response_object.get('KeyAlgorithm')),
            key_container_dn=CodeSign.InfoValue(response_object.get('KeyContainerDN')),
            key_storage_location=CodeSign.InfoValue(response_object.get('KeyStorageLocation')),
            key_use_flow_dn=response_object.get('KeyUseFlowDN'),
            max_uses=CodeSign.InfoValue(response_object.get('MaxUses')),
            type=response_object.get('Type'),
            visible_to=CodeSign.Items(response_object.get('VisibleTo')),
        )

    @staticmethod
    def GPGTemplate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.GPGTemplate(
            allow_user_key_import=response_object.get('AllowUserKeyImport'),
            authentication_key_algorithm=CodeSign.InfoValue(response_object.get('AuthenticationKeyAlgorithm')),
            dn=response_object.get('Dn'),
            email=CodeSign.InfoValue(response_object.get('Email')),
            encryption_key_algorithm=CodeSign.InfoValue(response_object.get('EncryptionKeyAlgorithm')),
            expiration=CodeSign.InfoValue(response_object.get('Expiration')),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            key_storage_location=CodeSign.InfoValue(response_object.get('KeyStorageLocation')),
            key_use_flow_dn=response_object.get('KeyUseFlowDN'),
            max_uses=CodeSign.InfoValue(response_object.get('MaxUses')),
            object_naming_pattern=response_object.get('ObjectNamingPattern'),
            per_user=response_object.get('PerUser'),
            real_name=CodeSign.InfoValue(response_object.get('RealName')),
            signing_key_algorithm=CodeSign.InfoValue(response_object.get('SigningKeyAlgorithm')),
            type=response_object.get('Type'),
            visible_to=CodeSign.Items(response_object.get('VisibleTo')),
        )

    @staticmethod
    def GlobalConfiguration(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.GlobalConfiguration(
            approved_key_storage_locations=CodeSign.KeyStorageLocations(
                response_object.get('ApprovedKeyStorageLocations')
            ),
            available_key_storage_locations=CodeSign.KeyStorageLocations(
                response_object.get('AvailableKeyStorageLocations')
            ),
            default_ca_container=response_object.get('DefaultCAContainer'),
            default_certificate_container=response_object.get('DefaultCertificateContainer'),
            default_credential_container=response_object.get('DefaultCredentialContainer'),
            key_use_timeout=response_object.get('KeyUseTimeout'),
            project_description_tooltip=response_object.get('ProjectDescriptionTooltip'),
            request_in_progress_message=response_object.get('RequestInProgressMessage'),
        )

    @staticmethod
    def Project(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.Project(
            application_dns=CodeSign.Items(response_object.get('ApplicationDNs')),
            applications=[CodeSign.Application(a) for a in response_object.get('Applications')],
            auditors=CodeSign.Items(response_object.get('Auditors')),
            certificate_environments=[
                CodeSign.CertificateEnvironment(ce)
                for ce in response_object.get('CertificateEnvironments')
            ],
            collections=[
                CodeSign.SignApplicationCollection(c)
                for c in response_object.get('Collections')
            ],
            created_on=from_date_string(response_object.get('CreatedOn')),
            description=response_object.get('Description'),
            dn=response_object.get('Dn'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            key_use_approvers=CodeSign.Items(response_object.get('KeyUseApprovers')),
            key_users=CodeSign.Items(response_object.get('KeyUsers')),
            owners=CodeSign.Items(response_object.get('Owners')),
            status=response_object.get('Status'),
        )

    @staticmethod
    def Rights(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        rights = response_object.get('Rights')
        return codesign.Rights(
            none=rights == 0,
            admin=rights & 1 != 0,
            use=rights & 2 != 0,
            audit=rights & 4 != 0,
            owner=rights & 8 != 0,
            project_approval=rights & 16 != 0,
            application_admin=rights & 32 != 0,
            approve_use=rights & 64 != 0,
        )

    @staticmethod
    def SignApplicationCollection(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return codesign.SignApplicationCollection(
            description=response_object.get('Description'),
            dn=response_object.get('Dn'),
            guid=response_object.get('Guid'),
            hash=response_object.get('Hash'),
            id=response_object.get('Id'),
            location=response_object.get('Location'),
            permitted_argument_pattern=response_object.get('PermittedArgumentPattern'),
            signatory_issuer=response_object.get('SignatoryIssuer'),
            signatory_subject=response_object.get('SignatorySubject'),
            size=response_object.get('Size'),
            version=response_object.get('Version'),
        )
