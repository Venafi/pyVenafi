from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.proxy_base import ProxyBaseAttributes
from pytpp.attributes.top import TopAttributes
from pytpp.attributes.zone_base import ZoneBaseAttributes


class VenafiPlatformAttributes(ProxyBaseAttributes, TopAttributes, ZoneBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Venafi Platform"
	acme_fqdn = Attribute('ACME FQDN', min_version='17.2')
	aws_ec2_role_authorized_identities = Attribute('AWS EC2 Role Authorized Identities', min_version='20.4')
	activation_latency_threshold = Attribute('Activation Latency Threshold', min_version='21.3')
	activation_query_frequency = Attribute('Activation Query Frequency', min_version='21.3')
	activation_work_threshold = Attribute('Activation Work Threshold', min_version='21.3')
	allowed_protocol_version = Attribute('Allowed Protocol Version', min_version='16.2')
	aperture_fqdn = Attribute('Aperture FQDN', min_version='16.2')
	authserver_fqdn = Attribute('AuthServer FQDN', min_version='19.1')
	capabilities_asymmetric_key_generation = Attribute('Capabilities: Asymmetric Key Generation')
	certificate_origin = Attribute('Certificate Origin', min_version='19.1')
	certificate_verification = Attribute('Certificate Verification', min_version='17.2')
	certificate_verification_log_warnings = Attribute('Certificate Verification Log Warnings', min_version='18.1')
	check_crl = Attribute('Check CRL', min_version='17.2')
	client_enrollment_require_windows_authentication = Attribute('Client Enrollment Require Windows Authentication', min_version='15.2')
	client_id = Attribute('Client ID', min_version='20.3')
	current_upgrade_task = Attribute('Current Upgrade Task', min_version='20.1')
	disable_triggers = Attribute('Disable Triggers', min_version='17.2')
	display_name = Attribute('Display Name', min_version='20.1')
	est_options = Attribute('Est Options', min_version='20.1')
	hsm_fqdn = Attribute('HSM FQDN', min_version='19.2')
	heartbeat_interval = Attribute('Heartbeat Interval')
	ignore_identity = Attribute('Ignore Identity', min_version='21.2')
	interval = Attribute('Interval')
	keystore_cache_check = Attribute('KeyStore Cache Check', min_version='20.4')
	keystore_cache_lifetime = Attribute('KeyStore Cache Lifetime', min_version='20.4')
	keystore_cache_size = Attribute('KeyStore Cache Size', min_version='20.4')
	log_debug = Attribute('Log Debug')
	log_server = Attribute('Log Server')
	log_target = Attribute('Log Target')
	maximum_above_normal_priority_threads = Attribute('Maximum Above Normal Priority Threads', min_version='18.4')
	maximum_below_normal_priority_threads = Attribute('Maximum Below Normal Priority Threads', min_version='18.4')
	maximum_highest_priority_threads = Attribute('Maximum Highest Priority Threads', min_version='18.4')
	maximum_low_priority_threads = Attribute('Maximum Low Priority Threads', min_version='17.4')
	maximum_normal_priority_threads = Attribute('Maximum Normal Priority Threads', min_version='18.4')
	maximum_threads = Attribute('Maximum Threads')
	migration_task = Attribute('Migration Task', min_version='19.2')
	minimum_threads = Attribute('Minimum Threads')
	operational_certificate_dn = Attribute('Operational Certificate DN')
	options = Attribute('Options')
	pending_migration_task = Attribute('Pending Migration Task', min_version='19.2')
	portal_fqdn = Attribute('Portal FQDN', min_version='16.2')
	private_key_vault_id = Attribute('Private Key Vault Id', min_version='20.1')
	processing_enabled = Attribute('Processing Enabled', min_version='21.3')
	scep_fqdn = Attribute('SCEP FQDN', min_version='16.2')
	scep_allowed_identities = Attribute('Scep Allowed Identities')
	scep_certificate_authority = Attribute('Scep Certificate Authority')
	scep_challenge_password = Attribute('Scep Challenge Password')
	scep_encryption_certificate_authority = Attribute('Scep Encryption Certificate Authority')
	scep_encryption_ra_certificate = Attribute('Scep Encryption RA Certificate', min_version='18.3')
	scep_instant_retries_client_user_agent = Attribute('Scep Instant Retries Client User Agent', min_version='19.3')
	scep_intune_application_id = Attribute('Scep Intune Application Id', min_version='19.3')
	scep_intune_application_secret = Attribute('Scep Intune Application Secret', min_version='19.3')
	scep_intune_authentication_authority_resource_url = Attribute('Scep Intune Authentication Authority Resource URL', min_version='19.3')
	scep_intune_challenge_password_sanity_check_disabled = Attribute('Scep Intune Challenge Password Sanity Check Disabled', min_version='19.4')
	scep_intune_graph_resource_url = Attribute('Scep Intune Graph Resource URL', min_version='19.3')
	scep_intune_http_connection_lease_timeout = Attribute('Scep Intune Http Connection Lease Timeout', min_version='19.3')
	scep_intune_http_connection_limit = Attribute('Scep Intune Http Connection Limit', min_version='19.3')
	scep_intune_http_timeout = Attribute('Scep Intune Http Timeout', min_version='19.3')
	scep_intune_provider_name_and_version = Attribute('Scep Intune Provider Name And Version', min_version='19.3')
	scep_intune_resource_url = Attribute('Scep Intune Resource URL', min_version='19.3')
	scep_intune_tenant_name = Attribute('Scep Intune Tenant Name', min_version='19.3')
	scep_intune_validation_attempts = Attribute('Scep Intune Validation Attempts', min_version='19.3')
	scep_maximum_ndes_challenges = Attribute('Scep Maximum Ndes Challenges')
	scep_ndes_challenge_validity = Attribute('Scep Ndes Challenge Validity')
	scep_object_container = Attribute('Scep Object Container')
	scep_options = Attribute('Scep Options')
	scep_ra_certificate = Attribute('Scep RA Certificate')
	scep_signing_certificate_authority = Attribute('Scep Signing Certificate Authority')
	scep_signing_ra_certificate = Attribute('Scep Signing RA Certificate', min_version='18.3')
	standby_mode = Attribute('Standby Mode', min_version='21.3')
	start_time = Attribute('Start Time')
	time_stamping_certificate_dn = Attribute('Time Stamping Certificate DN', min_version='20.3')
	time_stamping_proxy_host_urls = Attribute('Time Stamping Proxy Host URLs')
	time_stamping_proxy_options = Attribute('Time Stamping Proxy Options', min_version='20.3')
	timestampserver_fqdn = Attribute('TimeStampServer FQDN', min_version='20.3')
	upgrade_details = Attribute('Upgrade Details', min_version='20.1')
	upgrade_status = Attribute('Upgrade Status', min_version='20.1')
	user_agent_windows_authentication_enabled = Attribute('User Agent Windows Authentication Enabled', min_version='18.2')
	vedclient_fqdn = Attribute('VEDClient FQDN', min_version='16.2')
	webadmin_fqdn = Attribute('WebAdmin FQDN', min_version='16.2')
	websdk_fqdn = Attribute('WebSDK FQDN', min_version='16.2')