from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class EngineRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Engine Root"
    acme_certificates_folder = Attribute('ACME Certificates Folder', min_version='21.4')
    acme_enabled = Attribute('ACME Enabled', min_version='21.4')
    adaptable_script_max_file_size = Attribute('Adaptable Script Max File Size', min_version='21.4')
    advanced_key_protect = Attribute('Advanced Key Protect', min_version='21.4')
    allow_acme_folder_creation = Attribute('Allow ACME Folder Creation', min_version='21.4')
    authentication_scheme = Attribute('Authentication Scheme', min_version='21.4')
    automatically_apply_filters = Attribute('Automatically Apply Filters', min_version='21.4')
    contract_renewal_date = Attribute('Contract Renewal Date', min_version='23.3')
    disabled_features = Attribute('Disabled Features', min_version='21.4')
    enable_acme_cert_history = Attribute('Enable ACME Cert History', min_version='23.1')
    flow_process_expiry = Attribute('Flow Process Expiry', min_version='21.4')
    key_pair_renewal_flow = Attribute('Key Pair Renewal Flow', min_version='21.4')
    known_cloud_service = Attribute('Known Cloud Service', min_version='21.4')
    known_cloud_service_region = Attribute('Known Cloud Service Region', min_version='21.4')
    large_tree_support = Attribute('Large Tree Support', min_version='21.4')
    managed_by_options = Attribute('Managed By Options', min_version='21.4')
    message_bus_credential = Attribute('Message Bus Credential', min_version='23.3')
    message_bus_instance = Attribute('Message Bus Instance', min_version='23.3')
    message_bus_port = Attribute('Message Bus Port', min_version='23.3')
    message_bus_server = Attribute('Message Bus Server', min_version='23.3')
    message_bus_tls = Attribute('Message Bus Tls', min_version='23.3')
    monitored_uri_verification_engine_info = Attribute('Monitored URI Verification Engine Info', min_version='21.4')
    monitored_uri_verification_identifier = Attribute('Monitored URI Verification Identifier', min_version='21.4')
    monitored_uri_verification_last_check = Attribute('Monitored URI Verification Last Check', min_version='21.4')
    monitored_uri_verification_last_notification = Attribute(
        'Monitored URI Verification Last Notification',
        min_version='21.4'
    )
    monitored_uri_verification_uri_identifier = Attribute(
        'Monitored URI Verification URI Identifier',
        min_version='21.4'
    )
    oam_enabled = Attribute('OAM Enabled', min_version='21.4')
    oam_headervar = Attribute('OAM HeaderVar', min_version='21.4')
    oam_logout_url = Attribute('OAM Logout Url', min_version='21.4')
    operating_environment = Attribute('Operating Environment', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
    pendo_events_last_sent = Attribute('Pendo Events Last Sent', min_version='21.4')
    require_password = Attribute('Require Password', min_version='21.4')
    revocation_check_issuer_dn = Attribute('Revocation Check Issuer DN', min_version='21.4')
    revocation_check_issuer_identifier = Attribute('Revocation Check Issuer Identifier', min_version='21.4')
    secret_key_renewal_flow = Attribute('Secret Key Renewal Flow', min_version='21.4')
    tn_aperture_plugin_vault_id = Attribute('TN Aperture Plugin Vault Id', min_version='21.4')
    tn_public_cas = Attribute('TN Public CAs', min_version='21.4')
    tn_widget_vault = Attribute('TN Widget Vault', min_version='21.4')
    teams_enabled = Attribute('Teams Enabled', min_version='21.4')
    teams_options = Attribute('Teams Options', min_version='21.4')
    teams_required = Attribute('Teams Required', min_version='21.4')
    time_stamping_certificate_dn = Attribute('Time Stamping Certificate DN', min_version='21.4')
    time_stamping_proxy_host_urls = Attribute('Time Stamping Proxy Host URLs', min_version='21.4')
    time_stamping_proxy_options = Attribute('Time Stamping Proxy Options', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    trusted_websdk_modules = Attribute('Trusted WebSDK Modules', min_version='21.4')
    usage_tracking = Attribute('Usage Tracking', min_version='21.4')
    websdk_options = Attribute('WebSDK Options', min_version='21.4')
    whitelisted_elevation_commands = Attribute('Whitelisted Elevation Commands', min_version='21.4')
    workflow_interval = Attribute('Workflow Interval', min_version='21.4')
    workflow_last_check = Attribute('Workflow Last Check', min_version='21.4')
