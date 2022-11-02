from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class SAMLProfileAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SAML Profile"
    allow_unsolicited_saml_response = Attribute('Allow Unsolicited SAML Response', min_version='20.3')
    application_url = Attribute('Application Url', min_version='20.3')
    binding_type = Attribute('Binding Type', min_version='20.3')
    clock_skew = Attribute('Clock Skew', min_version='20.3')
    default_return_url = Attribute('Default Return Url', min_version='20.3')
    disabled = Attribute('Disabled', min_version='20.3')
    idp_entity_id = Attribute('IdP Entity Id', min_version='20.3')
    idp_metadata_filename = Attribute('IdP Metadata Filename', min_version='20.4')
    idp_metadata_import_date = Attribute('IdP Metadata Import Date', min_version='20.4')
    idp_response_signing_certificate_dn = Attribute('IdP Response Signing Certificate DN', min_version='20.4')
    idp_response_signing_certificate_vault_id = Attribute('IdP Response Signing Certificate Vault Id', min_version='20.3')
    idp_signin_url = Attribute('IdP SignIn Url', min_version='20.3')
    idp_vendor = Attribute('IdP Vendor', min_version='20.4')
    min_incoming_signing_algorithm = Attribute('Min Incoming Signing Algorithm', min_version='20.3')
    nameid_format = Attribute('NameId Format', min_version='20.3')
    outbound_signing_algorithm = Attribute('Outbound Signing Algorithm', min_version='20.3')
    relay_state_used_as_return_url = Attribute('Relay State Used As Return Url', min_version='20.3')
    saml_assertion_encryption_requirement = Attribute('SAML Assertion Encryption Requirement', min_version='20.3')
    saml_response_signature_requirement = Attribute('SAML Response Signature Requirement', min_version='20.3')
    sp_decryption_certificate_credential = Attribute('SP Decryption Certificate Credential', min_version='20.3')
    sp_entity_id = Attribute('SP Entity Id', min_version='20.3')
    sp_entity_id_source = Attribute('SP Entity Id Source', min_version='20.3')
    sp_signing_certificate_credential = Attribute('SP Signing Certificate Credential', min_version='20.3')
    sign_authn_requests = Attribute('Sign Authn Requests', min_version='20.3')
