from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class SSHCATemplateAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH CA Template"
    allow_private_key_reuse = Attribute('Allow Private Key Reuse')
    allow_to_specify_certificate_identifier_on_request = Attribute('Allow To Specify Certificate Identifier On Request')
    allow_to_specify_extensions_on_request = Attribute('Allow To Specify Extensions On Request')
    allow_to_specify_force_command_on_request = Attribute('Allow To Specify Force Command On Request')
    allow_to_specify_principals_on_request = Attribute('Allow To Specify Principals On Request')
    allow_to_specify_source_addresses_on_request = Attribute('Allow To Specify Source Addresses On Request')
    allowed_custom_extensions = Attribute('Allowed Custom Extensions')
    allowed_extension = Attribute('Allowed Extension')
    allowed_forced_command_pattern = Attribute('Allowed Forced Command Pattern')
    allowed_principal_pattern = Attribute('Allowed Principal Pattern')
    allowed_private_key_algorithm = Attribute('Allowed Private Key Algorithm')
    allowed_source_address = Attribute('Allowed Source Address')
    certificate_container = Attribute('Certificate Container')
    certificate_identifier = Attribute('Certificate Identifier')
    certificate_issuance_timeout_before_returning_pending_response = Attribute(
        'Certificate Issuance Timeout Before Returning Pending Response'
    )
    certificate_object_naming_pattern = Attribute('Certificate Object Naming Pattern')
    certificate_type = Attribute('Certificate Type')
    extension = Attribute('Extension')
    fingerprint_sha256 = Attribute('Fingerprint SHA256')
    force_command = Attribute('Force Command')
    hash_algorithm = Attribute('Hash Algorithm')
    include_issued_certificate_in_request = Attribute('Include Issued Certificate In Request')
    include_requester_identity_to_contacts = Attribute('Include Requester Identity to Contacts')
    key_algorithm = Attribute('Key Algorithm')
    key_id_format = Attribute('Key ID Format')
    maximum_age = Attribute('Maximum Age')
    principal = Attribute('Principal')
    public_signing_key_vault_id = Attribute('Public Signing Key Vault Id')
    ssh_certificate_issuance_flow = Attribute('SSH Certificate Issuance Flow')
    signing_key_algorithm = Attribute('Signing Key Algorithm')
    signing_key_dn = Attribute('Signing Key DN')
    source_address = Attribute('Source Address')
    use_certificate_object_naming_pattern = Attribute('Use Certificate Object Naming Pattern')
