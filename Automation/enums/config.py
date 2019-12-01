class ConfigClass:
    policy = 'Policy'


class FolderAttributes:
    certificate_origin = 'Certificate Origin'
    contact = 'Contact'
    created_by = 'Created By'
    description = 'Description'
    disabled = 'Disabled'
    escalation_contact = 'Escalation Contact'
    guid = 'GUID'
    log_view_server = 'Log View Server'
    managed_by = 'Managed By'
    master_preferences = 'Master Preferences'
    metadata = 'Metadata'
    reference = 'Reference'
    scep_ca_ident = 'Scep CA Ident'
    scep_certificate_authority = 'Scep Certificate Authority'
    scep_challenge_password = 'Scep Challenge Password'
    scep_encryption_ra_certificate = 'Scep Encryption RA Certificate'
    scep_intune_application_id = 'Scep Intune Application Id'
    scep_intune_application_secret = 'Scep Intune Application Secret'
    scep_intune_tenant_name = 'Scep Intune Tenant Name'
    scep_ra_certificate = 'Scep RA Certificate'
    scep_selection_rule = 'Scep Selection Rule'
    scep_signing_ra_certificate = 'Scep Signing RA Certificate'
    workflow = 'Workflow'
    workflow_block = 'Workflow Block'


class _CredentialAttributes:
    contact = 'Contact'
    created_by = 'Created By'
    description = 'Description'
    disabled = 'Disabled'
    escalation_contact = 'Escalation Contact'
    escalation_notice_interval = 'Escalation Notice Interval'
    escalation_notice_start = 'Escalation Notice Start'
    expiration_notice_interval = 'Expiration Notice Interval'
    expiration_notice_start = 'Expiration Notice Start'
    expiration = 'Expiration'
    guid = 'GUID'
    last_notification = 'Last Notification'
    managed_by = 'Managed By'
    metadata = 'Metadata'
    protection_key = 'Protection Key'
    reference = 'Reference'
    shared = 'Shared'
    vault_id = 'Vault Id'
    workflow = 'Workflow'
    workflow_block = 'Workflow Block'


class CredentialAttributes:
    class Amazon(_CredentialAttributes):
        authentication_credential = 'Authentication Credential'
        region_code = 'Region Code'
        role = 'Role'
        username = 'Username'
        web_service_url = 'Web Service URL'

    class Certificate(_CredentialAttributes):
        certificate = 'Certificate'
        username = 'Username'

    class Generic(_CredentialAttributes):
        pass

    class Password(_CredentialAttributes):
        pass

    class PrivateKey(_CredentialAttributes):
        username = 'Username'

    class UsernamePassword(_CredentialAttributes):
        username = 'Username'



# Example format for config enums

# class _Device:
#     pass
#
#
# class Devices:
#     class JumpServer(_Device):
#         pass
#
#
# class _Application:
#     pass
#
#
# class Applications:
#     class PKCS11(_Application):
#         pass
#
# attrs = {
#     Applications.PKCS11.dn: '\\asdfasdf\\asdfasdf'
# }
# app.create(..., attrs)
