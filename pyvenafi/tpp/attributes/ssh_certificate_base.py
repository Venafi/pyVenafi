from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.monitoring_base import MonitoringBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes

class SSHCertificateBaseAttributes(MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Certificate Base"
    certificate_identifier = Attribute('Certificate Identifier', min_version='21.4')
    certificate_vault_id = Attribute('Certificate Vault Id', min_version='21.4')
    destination_address = Attribute('Destination Address', min_version='21.4')
    error_message = Attribute('Error Message', min_version='21.4')
    extension = Attribute('Extension', min_version='21.4')
    force_command = Attribute('Force Command', min_version='21.4')
    hash_algorithm = Attribute('Hash Algorithm', min_version='21.4')
    in_error = Attribute('In Error', min_version='21.4')
    key_algorithm = Attribute('Key Algorithm', min_version='21.4')
    key_id = Attribute('Key ID', min_version='21.4')
    management_type = Attribute('Management Type', min_version='23.3')
    origin = Attribute('Origin', min_version='21.4')
    originating_ip = Attribute('Originating IP', min_version='21.4')
    principal = Attribute('Principal', min_version='21.4')
    private_key_vault_id = Attribute('Private Key Vault Id', min_version='21.4')
    private_signing_key_vault_id = Attribute('Private Signing Key Vault Id', min_version='21.4')
    public_key_hash = Attribute('Public Key Hash', min_version='21.4')
    public_key_vault_id = Attribute('Public Key Vault Id', min_version='21.4')
    requested_by = Attribute('Requested By', min_version='21.4')
    ssh_ca_template_dn = Attribute('SSH CA Template DN', min_version='21.4')
    ssh_certificate_issuance_flow = Attribute('SSH Certificate Issuance Flow', min_version='21.4')
    serial = Attribute('Serial', min_version='21.4')
    signing_key_fingerprint_sha256 = Attribute('Signing Key Fingerprint SHA256', min_version='21.4')
    source_address = Attribute('Source Address', min_version='21.4')
    stage = Attribute('Stage', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
    valid_from = Attribute('Valid From', min_version='21.4')
    valid_to = Attribute('Valid To', min_version='21.4')
    validity_period = Attribute('Validity Period', min_version='21.4')
