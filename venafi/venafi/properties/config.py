# region Application
class _ApplicationAttributesBase:
    adaptable_workflow_approvers = "Adaptable Workflow Approvers"
    adaptable_workflow_reference_id = "Adaptable Workflow Reference ID"
    adaptable_workflow_stage = "Adaptable Workflow Stage"
    agent_validate_now = "Agent Validate Now"
    approver = "Approver"
    certificate = "Certificate"
    certificate_file = "Certificate File"
    certificate_installed = "Certificate Installed"
    concurrent_connection_limit = "Concurrent Connection Limit"
    connection_method = "Connection Method"
    contact = "Contact"
    created_by = "Created By"
    credential = "Credential"
    description = "Description"
    disabled = "Disabled"
    discovered_by_dn = "Discovered By DN"
    discovered_on = "Discovered On"
    driver_arguments = "Driver Arguments"
    driver_name = "Driver Name"
    enforce_known_host = "Enforce Known Host"
    escalation_contact = "Escalation Contact"
    file_owner_group = "File Owner: Group"
    file_owner_user = "File Owner: User"
    file_permissions_group = "File Permissions: Group"
    file_permissions_user = "File Permissions: User"
    file_permissions_enabled = "File Permissions Enabled"
    file_validation_error = "File Validation Error"
    file_validation_result = "File Validation Result"
    global_sudo = "Global sudo"
    grouping_id = "Grouping Id"
    guid = "GUID"
    host = "Host"
    in_error = "In Error"
    in_process = "In Process"
    key_encryption_algorithm = "Key Encryption Algorithm"
    key_store_vault_id = "Key Store Vault Id"
    last_known_fingerprint = "Last Known Fingerprint"
    last_known_key_type = "Last Known Key Type"
    last_pushed_by = "Last Pushed By"
    last_pushed_on = "Last Pushed On"
    last_validation = "Last Validation"
    last_validation_result = "Last Validation Result"
    managed_by = "Managed By"
    metadata = "Metadata"
    port = "Port"
    private_key_password_credential = "Private Key Password Credential"
    rank = "Rank"
    reference = "Reference"
    remote_one_to_many_generation = "Remote One To Many Generation"
    remote_server_type = "Remote Server Type"
    restart_application = "Restart Application"
    secondary_credential = "Secondary Credential"
    ssl_listen_host = "SSL Listen Host"
    ssl_listen_port = "SSL Listen Port"
    stage = "Stage"
    status = "Status"
    sudo_password_delay = "Sudo Password Delay"
    temp_directory = "Temp Directory"
    terminal_columns = "Terminal Columns"
    terminal_rows = "Terminal Rows"
    terminal_type = "Terminal Type"
    ticket_dn = "Ticket DN"
    timeout = "Timeout"
    trusted_fingerprint = "Trusted Fingerprint"
    trusted_key_type = "Trusted Key Type"
    use_specified_host = "Use Specified Host"
    validation_disabled = "Validation Disabled"
    validation_errors = "Validation Errors"
    validation_results = "Validation Results"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class ApplicationAttributes(_ApplicationAttributesBase):
    class A10AXTrafficManager:
        bundle_certificate = "Bundle Certificate"
        certificate_chain_name = "Certificate Chain Name"
        certificate_name = "Certificate Name"
        file_validation_disabled = "File Validation Disabled"
        install_chain_file = "Install Chain File"
        network_validation_disabled = "Network Validation Disabled"
        ssh_port = "SSH Port"
        ssl_cache_size = "SSL Cache Size"
        ssl_close_notification = "SSL Close Notification"
        ssl_false_start = "SSL False Start"
        ssl_pass_phrase = "SSL Pass Phrase"
        ssl_profile_name = "SSL Profile Name"
        ssl_profile_type = "SSL Profile Type"
        tls_version = "TLS Version"
        use_ssl_template = "Use SSL Template"

    class Adaptable:
        certificate_name = "Certificate Name"
        file_validation_disabled = "File Validation Disabled"
        installation_status = "Installation Status"
        log_debug = "Log Debug"
        network_validation_disabled = "Network Validation Disabled"
        option_1 = "Option 1"
        option_2 = "Option 2"
        password_1 = "Password 1"
        pk_credential = "PK Credential"
        powershell_script = "PowerShell Script"
        powershell_script_hash_vault_id = "PowerShell Script Hash Vault Id"
        retry_after_script_hash_mismatch = "Retry After Script Hash Mismatch"
        script_hash_mismatch_error = "Script Hash Mismatch Error"
        secondary_credential = "Secondary Credential"
        text_field_1 = "Text Field 1"
        text_field_2 = "Text Field 2"
        text_field_3 = "Text Field 3"
        text_field_4 = "Text Field 4"
        text_field_5 = "Text Field 5"

    class AmazonAWS:
        access_key_id = "Access Key ID"
        aws_credential_dn = "Aws Credential DN"
        binding_target = "Binding Target"
        certificate_arn = "Certificate ARN"
        certificate_name = "Certificate Name"
        cloud_front_distribution_id = "CloudFront Distribution ID"
        create_binding = "Create Binding"
        file_validation_disabled = "File Validation Disabled"
        iam_certificate_id = "IAM Certificate ID"
        initial_binding_attempt = "Initial Binding Attempt"
        install_path = "Install Path"
        issued_by_aws = "Issued By AWS"
        load_balancer_name = "Load Balancer Name"
        load_balancer_port = "Load Balancer Port"
        load_balancer_region_code = "Load Balancer Region Code"
        network_validation_disabled = "Network Validation Disabled"
        provisioning_to = "Provisioning To"
        region_code = "Region Code"
        replace_store = "Replace Store"
        secret_access_key = "Secret Access Key"
        target_group = "Target Group"
        timeout = "Timeout"

    class AzureKeyVault:
        binding_hostnames = "Binding Hostnames"
        binding_ssl_type = "Binding SSL Type"
        certificate_credential = "Certificate Credential"
        certificate_name = "Certificate Name"
        client_id = "Client ID"
        create_binding = "Create Binding"
        create_san_dns_bindings = "Create SAN DNS Bindings"
        file_validation_disabled = "File Validation Disabled"
        network_validation_disabled = "Network Validation Disabled"
        non_exportable = "Non-Exportable"
        timeout = "Timeout"
        update_web_app = "Update Web App"
        vault_name = "Vault Name"
        web_app_name = "Web App Name"

    class Apache:
        application_id = "Application ID"
        certificate_chain_file = "Certificate Chain File"
        certificate_file = "Certificate File"
        client_tools_path = "Client Tools Path"
        file_validation_disabled = "File Validation Disabled"
        network_validation_disabled = "Network Validation Disabled"
        ocs_identifier = "OCS Identifier"
        overwrite_existing_chain = "Overwrite Existing Chain"
        partition_password_credential = "Partition Password Credential"
        private_key_file = "Private Key File"
        private_key_label = "Private Key Label"
        private_key_location = "Private Key Location"
        protection_type = "Protection Type"
        slot_number = "Slot Number"
        softcard_identifier = "Softcard Identifier"

    class Basic:
        certificate_file = "Certificate File"
        network_validation_disabled = "Network Validation Disabled"

    class BlueCoatSSLVA:
        certificate_label = "Certificate Label"
        certificate_oid = "Certificate OID"
        certificate_only = "Certificate Only"
        create_lists = "Create Lists"
        device_certificate = "Device Certificate"
        file_validation_disabled = "File Validation Disabled"
        key_store = "Key Store"
        network_validation_disabled = "Network Validation Disabled"
        replace_store = "Replace Store"

    class CAPI:
        binding_ip_address = "Binding IP Address"
        binding_port = "Binding Port"
        create_binding = "Create Binding"
        crypto_service_provider = "Crypto Service Provider"
        file_validation_disabled = "File Validation Disabled"
        friendly_name = "Friendly Name"
        hostname = "Hostname"
        log_windows_events = "Log Windows Events"
        network_validation_disabled = "Network Validation Disabled"
        non_exportable = "Non-Exportable"
        private_key_label = "Private Key Label"
        private_key_location = "Private Key Location"
        private_key_trustee = "Private Key Trustee"
        update_iis = "Update IIS"
        web_site_name = "Web Site Name"

    class CitrixNetScaler:
        certificate_file = "Certificate File"
        chain_cert = "Chain Cert"
        file_validation_disabled = "File Validation Disabled"
        fips_key = "Fips Key"
        import_only = "Import Only"
        issuer_certificate_name = "Issuer Certificate Name"
        max_filesize = "Max Filesize"
        network_validation_disabled = "Network Validation Disabled"
        private_key_file = "Private Key File"
        sni_certificate = "SNI Certificate"
        ssl_object_type = "SSL Object Type"
        temp_certificate_label = "Temp Certificate Label"
        virtual_server_name = "Virtual Server Name"

    class ConnectDirect:
        certificate_label = "Certificate Label"
        certificate_only = "Certificate Only"
        file_validation_disabled = "File Validation Disabled"
        key_store = "Key Store"
        key_store_credential = "Key Store Credential"
        network_validation_disabled = "Network Validation Disabled"
        node_name = "Node Name"
        protocol = "Protocol"

    class F5AuthenticationBundle:
        advanced_settings_bundle_name = "Advanced Settings Bundle Name"
        certificates = "Certificates"

    class F5LTMAdvanced:
        advanced_settings_bundle_name = "Advanced Settings Bundle Name"
        advertised_ca = "Advertised CA"
        archive_location = "Archive Location"
        authentication_frequency = "Authentication Frequency"
        build = "Build"
        bundle_certificate = "Bundle Certificate"
        bundle_certificate_collection = "Bundle Certificate Collection"
        certificate_chain_name = "Certificate Chain Name"
        certificate_name = "Certificate Name"
        chain_traversal_depth = "Chain Traversal Depth"
        client_authentication_certificate = "Client Authentication Certificate"
        config_sync = "Config Sync"
        connection_attempts = "Connection Attempts"
        crl = "CRL"
        delete_previous_cert_and_key = "Delete Previous Cert And Key"
        device_certificate = "Device Certificate"
        file_validation_disabled = "File Validation Disabled"
        fips_key = "Fips Key"
        force_profile_update = "Force Profile Update"
        install_chain_file = "Install Chain File"
        last_used_host = "Last Used Host"
        network_validation_disabled = "Network Validation Disabled"
        overwrite_certificate = "Overwrite Certificate"
        overwrite_existing_chain = "Overwrite Existing Chain"
        parent_ssl_profile_name = "Parent SSL Profile Name"
        partition = "Partition"
        previous_certificate = "Previous Certificate"
        previous_key = "Previous Key"
        provisioning_to = "Provisioning To"
        server_authentication_certificate = "Server Authentication Certificate"
        server_authentication_name = "Server Authentication Name"
        sni_default = "SNI Default"
        sni_server_name = "SNI Server Name"
        ssh_port = "SSH Port"
        ssl_profile_name = "SSL Profile Name"
        ssl_profile_type = "SSL Profile Type"
        system_id = "System Id"
        trusted_ca = "Trusted CA"
        use_advanced_settings = "Use Advanced Settings"
        use_basic_provisioning = "Use Basic Provisioning"
        version = "Version"
        virtual_server_name = "Virtual Server Name"
        virtual_server_partition = "Virtual Server Partition"

    class IBMDataPower:
        application_domain = "Application Domain"
        associate_to_cp = "Associate To CP"
        certificate_name = "Certificate Name"
        certificate_only = "Certificate Only"
        chain_cert = "Chain Cert"
        create_cp = "Create CP"
        create_ic = "Create IC"
        create_vc = "Create VC"
        credential_type = "Credential Type"
        crypto_profile = "Crypto Profile"
        file_validation_disabled = "File Validation Disabled"
        fips_key = "Fips Key"
        folder = "Folder"
        ftp_credential = "FTP Credential"
        ftp_host = "FTP Host"
        ftp_path = "FTP Path"
        ftp_port = "FTP Port"
        max_filesize = "Max Filesize"
        network_validation_disabled = "Network Validation Disabled"
        private_key_name = "Private Key Name"
        ssh_prompt = "SSH Prompt"
        ssl_profile_type = "SSL Profile Type"
        ssl_proxy_profile = "SSL Proxy Profile"
        temp_certificate_label = "Temp Certificate Label"
        use_basic_provisioning = "Use Basic Provisioning"
        xml_port = "XML Port"

    class IBMGSK:
        backup_store = "Backup Store"
        certificate_label = "Certificate Label"
        create_store = "Create Store"
        default_cert = "Default Cert"
        disable_ssh_history = "Disable SSH History"
        file_validation_disabled = "File Validation Disabled"
        fips_key = "Fips Key"
        hide_command_line_passwords = "Hide Command Line Passwords"
        java_home_path = "Java Home Path"
        key_store = "Key Store"
        key_store_credential = "Key Store Credential"
        key_store_validation_disabled = "Key Store Validation Disabled"
        network_validation_disabled = "Network Validation Disabled"
        password_expire_days = "Password Expire Days"
        recycle_alias = "Recycle Alias"
        refresh_security = "Refresh Security"
        replace_store = "Replace Store"
        stash_password = "Stash Password"
        store_type = "Store Type"
        temp_certificate_label = "Temp Certificate Label"
        utility_path = "Utility Path"
        version = "Version"

    class ImpervaMX:
        file_validation_disabled = "File Validation Disabled"
        key_store_validation_disabled = "Key Store Validation Disabled"
        private_key_name = "Private Key Name"
        server_group = "Server Group"
        service = "Service"
        site = "Site"
        username_credential = "Username Credential"
        utility_path = "Utility Path"

    class JKS:
        certificate_label = "Certificate Label"
        create_store = "Create Store"
        disable_ssh_history = "Disable SSH History"
        file_validation_disabled = "File Validation Disabled"
        java_vendor = "Java Vendor"
        key_algorithm = "Key Algorithm"
        key_store = "Key Store"
        key_store_credential = "Key Store Credential"
        key_store_validation_disabled = "Key Store Validation Disabled"
        keytool_path = "Keytool Path"
        network_validation_disabled = "Network Validation Disabled"
        private_key_location = "Private Key Location"
        protection_type = "Protection Type"
        recycle_alias = "Recycle Alias"
        replace_store = "Replace Store"
        slot_number = "Slot Number"
        softcard_identifier = "Softcard Identifier"
        store_type = "Store Type"
        temp_certificate_label = "Temp Certificate Label"
        version = "Version"

    class JuniperSAS:
        external_port = "External Port"
        file_validation_disabled = "File Validation Disabled"
        internal_port = "Internal Port"
        network_validation_disabled = "Network Validation Disabled"
        reassign_ports = "Reassign Ports"
        vlan_port = "Vlan Port"

    class OracleIPlanet:
        alias = "Alias"
        certutil_path = "Certutil Path"
        create_store = "Create Store"
        create_virtual_server = "Create Virtual Server"
        database_credential = "Database Credential"
        database_prefix = "Database Prefix"
        database_type = "Database Type"
        database_validation_disabled = "Database Validation Disabled"
        document_root = "Document Root"
        file_validation_disabled = "File Validation Disabled"
        install_path = "Install Path"
        key_store = "Key Store"
        key_store_credential = "Key Store Credential"
        mta_host = "MTA Host"
        network_validation_disabled = "Network Validation Disabled"
        pk12util_path = "Pk12util Path"
        protocol = "Protocol"
        replace_store = "Replace Store"
        secure_server_name = "Secure Server Name"
        use_proxy = "Use Proxy"
        virtual_server_dns_value = "Virtual Server DNS Value"
        virtual_server_port = "Virtual Server Port"
        virtual_server_user = "Virtual Server User"
        web_credential = "Web Credential"
        web_port = "Web Port"

    class PaloAltoNetworkFW:
        certificate_only = "Certificate Only"
        chain_cert = "Chain Cert"
        create_decryption_policy = "Create Decryption Policy"
        decryption_destinations = "Decryption Destinations"
        decryption_policy = "Decryption Policy"
        decryption_profile = "Decryption Profile"
        file_validation_disabled = "File Validation Disabled"
        lock_config = "Lock Config"
        network_validation_disabled = "Network Validation Disabled"
        replace_store = "Replace Store"
        temporary_name = "Temporary Name"

    class PEM:
        certificate_chain_file = "Certificate Chain File"
        certificate_file = "Certificate File"
        file_validation_disabled = "File Validation Disabled"
        key_store = "Key Store"
        network_validation_disabled = "Network Validation Disabled"
        overwrite_existing_chain = "Overwrite Existing Chain"
        private_key_file = "Private Key File"

    class PKCS11:
        hsm_cblob = 'HSM:CBlob'
        hsm_cka_label_format = 'HSM:CKA LABEL Format'
        hsm_csr_subject_dn = 'HSM:CSR Subject DN'
        hsm_certificate_directory = 'HSM:Certificate Directory'
        hsm_client_tool_path = 'HSM:Client Tool Path'
        hsm_cryptoki_file = 'HSM:Cryptoki File'
        hsm_embed_sans_in_csr = 'HSM:Embed SANs in CSR'
        hsm_ic_cka_label_format = 'HSM:IC CKA LABEL Format'
        hsm_import_certificate = 'HSM:Import Certificate'
        hsm_issued_id = 'HSM:Issued ID'
        hsm_issued_label = 'HSM:Issued Label'
        hsm_issued_usecase = 'HSM:Issued Usecase'
        hsm_kpblob = 'HSM:KPBlob'
        hsm_last_issued_cblob = 'HSM:Last Issued CBlob'
        hsm_last_issued_id = 'HSM:Last Issued ID'
        hsm_last_issued_kpblob = 'HSM:Last Issued KPBlob'
        hsm_last_issued_label = 'HSM:Last Issued Label'
        hsm_last_issued_usecase = 'HSM:Last Issued Usecase'
        hsm_openssl_config_file = 'HSM:Openssl Config File'
        hsm_openssl_path = 'HSM:Openssl Path'
        hsm_openssl_type = 'HSM:Openssl Type'
        hsm_pkcs11attributes = 'HSM:PKCS11Attributes'
        hsm_protection_type = 'HSM:Protection Type'
        hsm_requested_cka_label = 'HSM:Requested CKA LABEL'
        hsm_requested_ecdh = 'HSM:Requested ECDH'
        hsm_requested_usecase = 'HSM:Requested Usecase'
        hsm_reverse_subject_dn = 'HSM:Reverse Subject DN'
        hsm_tmp_issued_cblob = 'HSM:TMP Issued CBlob'
        hsm_tmp_issued_id = 'HSM:TMP Issued ID'
        hsm_tmp_issued_kpblob = 'HSM:TMP Issued KPBlob'
        hsm_token_label = 'HSM:Token Label'
        hsm_token_password = 'HSM:Token Password'

    class PKCS12:
        bundle_certificate = "Bundle Certificate"
        certificate_chain_file = "Certificate Chain File"
        certificate_file = "Certificate File"
        create_store = "Create Store"
        file_validation_disabled = "File Validation Disabled"
        friendly_name = "Friendly Name"
        key_store = "Key Store"
        key_store_credential = "Key Store Credential"
        network_validation_disabled = "Network Validation Disabled"
        recycle_alias = "Recycle Alias"
        replace_store = "Replace Store"

    class RiverbedSteelHead:
        certificate_type = "Certificate Type"
        file_validation_disabled = "File Validation Disabled"
        install_chain = "Install Chain"
        network_validation_disabled = "Network Validation Disabled"
        replace_existing = "Replace Existing"

    class TealeafPCA:
        file_validation_disabled = "File Validation Disabled"
        install_path = "Install Path"
        key_store_credential = "Key Store Credential"
        key_store_name = "Key Store Name"
        key_store_validation_disabled = "Key Store Validation Disabled"
        sunimp_utility_path = "Sunimp Utility Path"
        tealeaf_utility_path = "Tealeaf Utility Path"

    class VAMnShield:
        file_validation_disabled = "File Validation Disabled"
        install_path = "Install Path"
        key_store_validation_disabled = "Key Store Validation Disabled"
        km_local_path = "KM Local Path"
        module_id = "Module Id"


class _ApplicationAttributeValuesBase:
    class ConnectionMethod:
        https = 'HTTPS'
        ssh = 'SSH'
        winrm = 'WinRM'
        winrms = 'WinRMs'

    class GroupPermissions:
        none = '0000'
        read_only = '0040'
        read_and_write = '0060'

    class ManagedBy:
        aperture = 'Aperture'
        user_portal = 'User Portal'

    class OwnerPermissions:
        read_only = '0400'
        read_and_write = '0600'

    class ProtectionType:
        module = 'Module'
        ocs = 'OCS'
        softcard = 'softcard'


class ApplicationAttributeValues(_ApplicationAttributeValuesBase):
    class A10AXTrafficManager:
        class TemplateType:
            client = 'Client'
            server = 'Server'

        class ServerSslTlsVersion:
            ssl_3_0 = 'SSL Version 3.0'
            tls_1_0 = 'TLS Version 1.0'

    class AmazonAWS:
        class BindingTarget:
            no_binding = 0
            elastic_load_balancer = 1
            cloud_front = 2
            application_load_balancer = 3

        class ProvisionTo:
            acm = 'ACM'
            iam = 'IAM'

        class Region:
            us_east_virginia = 'us-east-1'
            us_east_ohio = 'us-east-2'
            us_west_california = 'us-west-1'
            us_west_oregon = 'us-west-2'
            asian_pacific_tokyo = 'ap-northeast-1'
            asian_pacific_seoul = 'ap-northeast-2'
            asian_pacific_osaka_local = 'ap-northeast-3'
            asian_pacific_mumbai = 'ap-south-1'
            asian_pacific_singapore = 'ap-southeast-1'
            asian_pacific_sydney = 'ap-southeast-2'
            canada = 'ca-central-1'
            eu_frankfurt = 'eu-central-1'
            eu_ireland = 'eu-west-1'
            eu_london = 'eu-west-2'
            eu_paris = 'eu-west-3'
            south_america_sao_paolo = 'sa-east-1'
            aws_govcloud_us = 'us-gov-west-1'

    class Apache:
        class PrivateKeyLocation:
            device = 'Device'
            gemalto_safe_net_hsm = 'Gemalto SafeNet HSM'
            thales_nshield_hsm = "Thales nShield HSM"

    class AzureKeyVault:
        class SslTye:
            sni = 0
            ip_based = 1

    class CAPI:
        class PrivateKeyLocation:
            device = 'Device'
            gemalto_safe_net_hsm = 'Gemalto SafeNet HSM'
            thales_nshield_hsm = "Thales nShield HSM"

    class CitrixNetScaler:
        class BindCertificateTo:
            virtual_server = 'Virtual Server'
            service = 'Service'
            service_group = 'Service Group'

    class ConnectDirect:
        class APIProtocol:
            ssl = 'SSL'
            tls = 'TLS'
            tls_1_1 = 'TLS11'
            tls_1_2 = 'TLS12'

    class F5LTMAdvanced:
        class ClientCertificate:
            ignore = 'Ignore'
            require = 'Require'
            request = 'Request'

        class Frequency:
            once = 'Once'
            always = 'Always'

        class ProvisioningMode:
            advanced = 0
            basic_with_configurable_certificate_name = 1
            basic_with_automatic_certificate_name = 2

        class ProvisioningTo:
            standalone = 'Standalone'
            active = 'Active'
            standby = 'Standby'
            ignore_failover_state = 'Ignore Failover State'

        class ServerCertificate:
            ignore = 'Ignore'
            require = 'Require'

        class SslProfileType:
            client = 'Client'
            server = 'Server'

    class IBMDataPower:
        class CertificateFolder:
            cert = 1
            shared_cert = 2

        class CredentialType:
            identification = 1
            validation = 2

        class ProfileType:
            ssl_proxy = 1
            ssl_client = 2
            ssl_server = 3

        class ProvisioningMode:
            advanced = 1
            basic = 2

    class IBMGSK:
        class Version:
            gsk_7_0 = 'GSK 7.0'
            gsk_8_0 = 'GSK 8.0'

    class JKS:
        class PrivateKeyLocation:
            device = 'Device'
            gemalto_safe_net_hsm = 'Gemalto SafeNet HSM'
            thales_nshield_hsm = "Thales nShield HSM"

        class JavaVendor:
            oracle = 'Oracle'
            ibm = 'IBM'

        class JavaVersion:
            java_1_6 = 'Java 1.6'
            java_1_7 = 'Java 1.7'
            java_1_8 = 'Java 1.8'

        class StoreType:
            jks = 'JKS'
            jceks = 'JCEKS'

    class OracleIPlanet:
        class CertificateDatabaseType:
            berkeley = 'Berkeley'
            sqlite = 'SQLite'

    class PaloAltoNetworkFW:
        class Provision:
            certificate_only = 1
            certificate_and_private_key = 2

    class PKCS11:
        class ImportCertificatesIntoHsm:
            zero = 0
            no = 'No'
            import_certificate_only = 'Import Certificate Only'
            import_certificate_and_chain = 'Import Certificate And Chain'
            import_certificate_with_intermediate_certificates = 'Import Certificate With Intermediate Certificates'

        class LabelFormat:
            date_with_cn = 'Date with CN'
            custom_label = 'Custom Label'

        class OpenSslType:
            custom_openssl_directory = 'Custom OpenSSL Directory'
            system = 'System'

        class UseCase:
            tls_client_ecc = 'TLS Client - ECC'
            tls_client_rsa = 'TLS Client - RSA'
            tls_client_server_ecc = 'TLS Client/Server - ECC'
            tls_client_server_rsa = 'TLS Client/Server - RSA'
            tls_client_server_rsa_ibm_jvm = 'TLS Client/Server - RSA - IBM JVM'
            tls_client_server_rsa_oracle_sun_jvm = 'TLS Client/Server - RSA - Oracle/Sun JVM'
            tls_server_ecc = 'TLS Server - ECC'
            tls_server_rsa = 'TLS Server - RSA'
            tls_server_rsa_ibm_jvm = 'TLS Server - RSA - IBM JVM'
            tls_server_rsa_oracle_sun_jvm = 'TLS Server - RSA - Oracle/Sun JVM'
            message_encryption_rsa = 'Message Encryption - RSA'
            message_signing_ecc = 'Message Signing - ECC'
            message_signing_rsa = 'Message Signing - RSA'
            code_signing_ecc = 'Code Signing - ECC'
            code_signing_rsa = 'Code Signing - RSA'
            key_derivation_ecc = 'Key Derivation - ECC'
            key_wrapping_rsa = 'Key Wrapping - RSA'

    class PKCS12:
        class CertificateChainLocation:
            certificate_chain_file = 0
            pkcs12_file = 1

    class RiverbedSteelHead:
        class CertificateType:
            ssl_main = 0
            secure_peering = 1
            web = 2


class ApplicationClassNames:
    a10_ax_traffic_manager = "A10 AX Traffic Manager"
    adaptable_app = "Adaptable App"
    amazon_app = "Amazon App"
    apache = "Apache"
    azure_key_vault = "Azure Key Vault"
    basic = "Basic"
    blue_coat_sslva = "BlueCoat SSLVA"
    brocade = "Brocade"
    capi = "CAPI"
    cisco_ace = "CiscoACE"
    cisco_csm = "CiscoCSM"
    cisco_css = "CiscoCSS"
    connect_direct = "ConnectDirect"
    data_power = "DataPower"
    f5 = "F5"
    f5_authentication_bundle = 'F5 Authentication Bundle'
    f5_ltm_advanced = "F5 LTM Advanced"
    gsk = "GSK"
    iis5 = "IIS5"
    iis6 = "IIS6"
    imperva_mx = "Imperva MX"
    iplanet = "iPlanet"
    jks = "JKS"
    juniper_sas = "Juniper SAS"
    layer_7_ssg = "Layer 7 SSG"
    net_scaler = "NetScaler"
    palo_alto_network_fw = "Palo Alto Network FW"
    pem = "PEM"
    pkcs11 = "PKCS11"
    pkcs12 = "PKCS#12"
    riverbed_steel_head = "Riverbed SteelHead"
    server_certificate_work = "Server Certificate Work"
    tealeaf_pca = "Tealeaf PCA"
    tealeafsunimp = "TealeafSunimp"
    vam_nshield = "VAM nShield"
    vam_cavium = "VamCavium"

# endregion


# region Certificate
class CertificateAttributes:
    acme_account_dn = "ACME Account DN"
    adaptable_ca_binary_data_vault_id = "Adaptable CA:Binary Data Vault ID"
    adaptable_ca_early_password_vault_id = "Adaptable CA:Early Password Vault ID"
    adaptable_ca_early_pkcs7_vault_id = "Adaptable CA:Early Pkcs7 Vault ID"
    adaptable_ca_early_private_key_vault_id = "Adaptable CA:Early Private Key Vault ID"
    adaptable_ca_script_hash_mismatch_error = "Adaptable CA:Script Hash Mismatch Error"
    adaptable_workflow_approvers = "Adaptable Workflow Approvers"
    adaptable_workflow_reference_id = "Adaptable Workflow Reference ID"
    adaptable_workflow_stage = "Adaptable Workflow Stage"
    address = "Address"
    allow_private_key_reuse = "Allow Private Key Reuse"
    amazon_ca_first_pickup_request = "Amazon CA:First Pickup Request"
    amazon_ca_timestamp = "Amazon CA:Timestamp"
    application_group_dn = "Application Group DN"
    approved_issuer = "Approved Issuer"
    approver = "Approver"
    certificate_authority = "Certificate Authority"
    certificate_download__pbes2_algorithm = "Certificate Download: PBES2 Algorithm"
    certificate_process_validator = "Certificate Process Validator"
    certificate_vault_id = "Certificate Vault Id"
    city = "City"
    comodo_ca_dcv_email = "Comodo CA:DCV Email"
    comodo_ca_server_type_id = "Comodo CA:Server Type Id"
    comodo_ccm_ca_pass_phrase = "Comodo CCM CA:Pass Phrase"
    comodo_ccm_ca_server_type = "Comodo CCM CA:Server Type"
    consumers = "Consumers"
    contact = "Contact"
    country = "Country"
    created_by = "Created By"
    creation_date = "Creation Date"
    csr_vault_id = "CSR Vault Id"
    description = "Description"
    detect_all_ssl_tls_protocols = "Detect All SSL TLS Protocols"
    digicert_ca_address = "DigiCert CA:Address"
    digicert_ca_request_id = "DigiCert CA:Request Id"
    digicert_ca_server_type = "DigiCert CA:Server Type"
    digicert_ca_specific_end_date = "DigiCert CA:Specific End Date"
    digicert_ca_zip = "DigiCert CA:Zip"
    disable_automatic_renewal = "Disable Automatic Renewal"
    disable_password_complexity = "Disable Password Complexity"
    disabled = "Disabled"
    discovered_by_dn = "Discovered By DN"
    discovered_on = "Discovered On"
    domain_suffix_whitelist = "Domain Suffix Whitelist"
    driver_arguments = "Driver Arguments"
    driver_name = "Driver Name"
    elliptic_curve = "Elliptic Curve"
    encryption_driver = "Encryption Driver"
    enforce_unique_subject = "Enforce Unique Subject"
    entrustnet_ca_additional_emails = "EntrustNET CA:Additional Emails"
    entrustnet_ca_additional_field_value = "EntrustNET CA:Additional Field Value"
    entrustnet_ca_email_address = "EntrustNET CA:Email Address"
    entrustnet_ca_first_name = "EntrustNET CA:First Name"
    entrustnet_ca_first_pickup_request = "EntrustNET CA:First Pickup Request"
    entrustnet_ca_last_name = "EntrustNET CA:Last Name"
    entrustnet_ca_specific_end_date = "EntrustNET CA:Specific End Date"
    entrustnet_ca_timestamp = "EntrustNET CA:Timestamp"
    escalation_contact = "Escalation Contact"
    escalation_notice_interval = "Escalation Notice Interval"
    escalation_notice_start = "Escalation Notice Start"
    esm_ca_override_default_key_update_policy = "ESM CA:Override Default Key Update Policy"
    expiration_notice_interval = "Expiration Notice Interval"
    expiration_notice_start = "Expiration Notice Start"
    fields = "Fields"
    file_validation_error = "File Validation Error"
    file_validation_result = "File Validation Result"
    generate_keypair_on_application = "Generate Keypair On Application"
    geotrust_ca_address = "GeoTrust CA:Address"
    geotrust_ca_admin_contact_address = "GeoTrust CA:Admin Contact Address"
    geotrust_ca_admin_contact_city = "GeoTrust CA:Admin Contact City"
    geotrust_ca_admin_contact_country = "GeoTrust CA:Admin Contact Country"
    geotrust_ca_admin_contact_email_address = "GeoTrust CA:Admin Contact Email Address"
    geotrust_ca_admin_contact_first_name = "GeoTrust CA:Admin Contact First Name"
    geotrust_ca_admin_contact_last_name = "GeoTrust CA:Admin Contact Last Name"
    geotrust_ca_admin_contact_organization = "GeoTrust CA:Admin Contact Organization"
    geotrust_ca_admin_contact_phone_number = "GeoTrust CA:Admin Contact Phone Number"
    geotrust_ca_admin_contact_postal_code = "GeoTrust CA:Admin Contact Postal Code"
    geotrust_ca_admin_contact_state = "GeoTrust CA:Admin Contact State"
    geotrust_ca_admin_contact_title = "GeoTrust CA:Admin Contact Title"
    geotrust_ca_authentication_comments = "GeoTrust CA:Authentication Comments"
    geotrust_ca_authentication_statuses = "GeoTrust CA:Authentication Statuses"
    geotrust_ca_enrollment_mode = "GeoTrust CA:Enrollment Mode"
    geotrust_ca_order_id = "GeoTrust CA:Order Id"
    geotrust_ca_postal_code = "GeoTrust CA:Postal Code"
    geotrust_ca_server_count = "GeoTrust CA:Server Count"
    geotrust_ca_server_type = "GeoTrust CA:Server Type"
    geotrust_ca_telephone_number = "GeoTrust CA:Telephone Number"
    geotrust_ca_timestamp = "GeoTrust CA:Timestamp"
    geotrust_enterprise_ca_address = "GeoTrust Enterprise CA:Address"
    geotrust_enterprise_ca_admin_contact_email_address = "GeoTrust Enterprise CA:Admin Contact Email Address"
    geotrust_enterprise_ca_admin_contact_first_name = "GeoTrust Enterprise CA:Admin Contact First Name"
    geotrust_enterprise_ca_admin_contact_last_name = "GeoTrust Enterprise CA:Admin Contact Last Name"
    geotrust_enterprise_ca_admin_contact_phone_number = "GeoTrust Enterprise CA:Admin Contact Phone Number"
    geotrust_enterprise_ca_admin_contact_title = "GeoTrust Enterprise CA:Admin Contact Title"
    geotrust_enterprise_ca_approver_email = "GeoTrust Enterprise CA:Approver Email"
    geotrust_enterprise_ca_enrollment_mode = "GeoTrust Enterprise CA:Enrollment Mode"
    geotrust_enterprise_ca_postal_code = "GeoTrust Enterprise CA:Postal Code"
    geotrust_enterprise_ca_server_count = "GeoTrust Enterprise CA:Server Count"
    geotrust_enterprise_ca_server_type = "GeoTrust Enterprise CA:Server Type"
    geotrust_enterprise_ca_telephone_number = "GeoTrust Enterprise CA:Telephone Number"
    geotrust_enterprise_ca_timestamp = "GeoTrust Enterprise CA:Timestamp"
    geotrusttrueflex_ca_emails = "GeotrustTrueFlex CA:Emails"
    geotrusttrueflex_ca_enrollment_mode = "GeotrustTrueFlex CA:Enrollment Mode"
    geotrusttrueflex_ca_first_pickup_request = "GeotrustTrueFlex CA:First Pickup Request"
    geotrusttrueflex_ca_timestamp = "GeotrustTrueFlex CA:Timestamp"
    given_name = "Given Name"
    globalsign_mssl_ca_email = "GlobalSign MSSL CA:Email"
    globalsign_mssl_ca_first_name = "GlobalSign MSSL CA:First Name"
    globalsign_mssl_ca_last_name = "GlobalSign MSSL CA:Last Name"
    globalsign_mssl_ca_phone = "GlobalSign MSSL CA:Phone"
    grouping_id = "Grouping Id"
    guid = "GUID"
    in_error = "In Error"
    in_process = "In Process"
    internet_email_address = "Internet EMail Address"
    issued_to = "Issued To"
    key_algorithm = "Key Algorithm"
    key_bit_strength = "Key Bit Strength"
    key_storage_location = "Key Storage Location"
    keynectis_sequoia_ca_fields = "Keynectis Sequoia CA:Fields"
    last_evaluated_on = "Last Evaluated On"
    last_notification = "Last Notification"
    last_renewed_by = "Last Renewed By"
    last_renewed_on = "Last Renewed On"
    last_validation = "Last Validation"
    last_validation_result = "Last Validation Result"
    last_validation_state_update = "Last Validation State Update"
    license_count = "License Count"
    managed_by = "Managed By"
    management_type = "Management Type"
    manual_approval = "Manual Approval"
    manual_csr = "Manual Csr"
    metadata = "Metadata"
    microsoft_ca_pool_certificate_authority = "Microsoft CA Pool:Certificate Authority"
    microsoft_ca_request_approved = "Microsoft CA:Request Approved"
    microsoft_ca_specific_end_date = "Microsoft CA:Specific End Date"
    network_validation_disabled = "Network Validation Disabled"
    notes = "Notes"
    notification_disabled = "Notification Disabled"
    opentrust_pki_ca_fields = "OpenTrust PKI CA:Fields"
    opentrust_pki_ca_first_pickup_request = "OpenTrust PKI CA:First Pickup Request"
    opentrust_pki_ca_requester_email = "OpenTrust PKI CA:Requester Email"
    options = "Options"
    organization = "Organization"
    organizational_unit = "Organizational Unit"
    origin = "Origin"
    pkcs10_hash_algorithm = "PKCS10 Hash Algorithm"
    portal_download_count = "Portal Download Count"
    postal_code = "Postal Code"
    private_key_vault_id = "Private Key Vault Id"
    prohibit_wildcard = "Prohibit Wildcard"
    prohibited_san_types = "Prohibited SAN Types"
    prohibited_subject_attributes = "Prohibited Subject Attributes"
    protection_key = "Protection Key"
    public_key_vault_id = "Public Key Vault Id"
    rank = "Rank"
    reference = "Reference"
    renewal_window = "Renewal Window"
    reverse_dc_order = "Reverse DC Order"
    revocation_check_disabled = "Revocation Check Disabled"
    revocation_check_in_error = "Revocation Check In Error"
    revocation_check_last_checked = "Revocation Check Last Checked"
    revocation_check_now = "Revocation Check Now"
    revocation_check_status = "Revocation Check Status"
    revocation_original_request = "Revocation Original Request"
    revocation_request = "Revocation Request"
    scep_transaction_id = "Scep Transaction Id"
    server_type = "Server Type"
    signing_request_subject = "Signing Request Subject"
    ssl_listen_host = "SSL Listen Host"
    ssl_listen_port = "SSL Listen Port"
    stage = "Stage"
    state = "State"
    status = "Status"
    surname = "Surname"
    symantec_lhk_ca_fields = "Symantec LHK CA:Fields"
    telephone = "Telephone"
    thawte_ca_emails = "Thawte CA:Emails"
    thawte_ca_enrollment_mode = "Thawte CA:Enrollment Mode"
    thawte_ca_first_pickup_request = "Thawte CA:First Pickup Request"
    thawte_ca_timestamp = "Thawte CA:Timestamp"
    ticket_dn = "Ticket DN"
    transaction_id = "Transaction Id"
    trusted_status = "Trusted Status"
    trustwave_ca_enrollment_mode = "Trustwave CA:Enrollment Mode"
    trustwave_ca_first_pickup_request = "Trustwave CA:First Pickup Request"
    trustwave_ca_timestamp = "Trustwave CA:Timestamp"
    use_common_name = "Use Common Name"
    use_dns_subjectaltname = "Use DNS SubjectAltName"
    use_specified_host = "Use Specified Host"
    validate_chain_returned_by_host = "Validate Chain Returned By Host"
    validation_disabled = "Validation Disabled"
    validation_errors = "Validation Errors"
    validation_results = "Validation Results"
    validation_state = "Validation State"
    validity_period = "Validity Period"
    verisign_ca_additional_field_value = "VeriSign CA:Additional Field Value"
    verisign_ca_challenge_credential = "VeriSign CA:Challenge Credential"
    verisign_ca_comment = "VeriSign CA:Comment"
    verisign_ca_enrollment_mode = "VeriSign CA:Enrollment Mode"
    verisign_ca_first_pickup_request = "VeriSign CA:First Pickup Request"
    verisign_ca_license_count = "VeriSign CA:License Count"
    verisign_ca_original_challenge_credential = "VeriSign CA:Original Challenge Credential"
    verisign_ca_replacement_reason = "VeriSign CA:Replacement Reason"
    verisign_ca_server_type = "VeriSign CA:Server Type"
    verisign_ca_specific_end_date = "VeriSign CA:Specific End Date"
    verisign_ca_timestamp = "VeriSign CA:Timestamp"
    verizon_ca_additional_field_value = "Verizon CA:Additional Field Value"
    verizon_ca_challenge_credential = "Verizon CA:Challenge Credential"
    verizon_ca_challenge_credential_hint = "Verizon CA:Challenge Credential Hint"
    verizon_ca_enrollment_mode = "Verizon CA:Enrollment Mode"
    verizon_ca_first_pickup_request = "Verizon CA:First Pickup Request"
    verizon_ca_license_count = "Verizon CA:License Count"
    verizon_ca_number_of_servers = "Verizon CA:Number Of Servers"
    verizon_ca_organization_summary = "Verizon CA:Organization Summary"
    verizon_ca_server_name = "Verizon CA:Server Name"
    verizon_ca_server_type = "Verizon CA:Server Type"
    verizon_ca_tech_email = "Verizon CA:Tech Email"
    verizon_ca_tech_firstname = "Verizon CA:Tech Firstname"
    verizon_ca_tech_surname = "Verizon CA:Tech Surname"
    verizon_ca_tech_telnumber = "Verizon CA:Tech Telnumber"
    verizon_ca_timestamp = "Verizon CA:Timestamp"
    want_renewal = "Want Renewal"
    work_dn = "Work DN"
    workflow = "Workflow"
    workflow_block = "Workflow Block"
    x509_d = "X509 D"
    x509_dc = "X509 DC"
    x509_dnq = "X509 DNQ"
    x509_e = "X509 E"
    x509_extension_fields = "X509 Extension Fields"
    x509_gn = "X509 GN"
    x509_gq = "X509 GQ"
    x509_i = "X509 I"
    x509_p = "X509 P"
    x509_pa = "X509 PA"
    x509_pc = "X509 PC"
    x509_sa = "X509 SA"
    x509_sn = "X509 SN"
    x509_sno = "X509 SNO"
    x509_subject = "X509 Subject"
    x509_subjectaltname = "X509 SubjectAltName"
    x509_subjectaltname_dns = "X509 SubjectAltName DNS"
    x509_subjectaltname_ipaddress = "X509 SubjectAltName IPAddress"
    x509_subjectaltname_othername_upn = "X509 SubjectAltName OtherName UPN"
    x509_subjectaltname_rfc822 = "X509 SubjectAltName RFC822"
    x509_subjectaltname_uri = "X509 SubjectAltName URI"
    x509_t = "X509 T"
    x509_tn = "X509 TN"
    x509_ua = "X509 UA"
    x509_uid = "X509 UID"
    x509_un = "X509 UN"
    xolphin_ca_address = "Xolphin CA:Address"
    xolphin_ca_approver_email_address = "Xolphin CA:Approver Email Address"
    xolphin_ca_approver_first_name = "Xolphin CA:Approver First Name"
    xolphin_ca_approver_last_name = "Xolphin CA:Approver Last Name"
    xolphin_ca_approver_phone_number = "Xolphin CA:Approver Phone Number"
    xolphin_ca_approver_type = "Xolphin CA:Approver Type"
    xolphin_ca_city = "Xolphin CA:City"
    xolphin_ca_company = "Xolphin CA:Company"
    xolphin_ca_country_code = "Xolphin CA:Country Code"
    xolphin_ca_department = "Xolphin CA:Department"
    xolphin_ca_effective_polling_interval = "Xolphin CA:Effective Polling Interval"
    xolphin_ca_kvk_number = "Xolphin CA:KvK Number"
    xolphin_ca_postbox = "Xolphin CA:Postbox"
    xolphin_ca_reference_number = "Xolphin CA:Reference Number"
    xolphin_ca_zip_code = "Xolphin CA:Zip Code"


class CertificateAttributeValues:
    class EllipticCurve:
        p256 = 'P256'
        p384 = 'P384'
        p521 = 'P521'

    class Format:
        base64 = 'Base64'
        pkcs8 = 'Base64 (PKCS #8)'
        der = 'DER'
        jks = 'JKS'
        pkcs7 = 'PKCS #7'
        pkcs12 = 'PKCS #12'

    class HashAlgorithm:
        sha1 = 'Sha1'
        sha256 = 'Sha256'

    class KeyAlgorithm:
        rsa = 'RSA'
        ecc = 'ECC'

    class ManagedBy:
        aperture = 'Aperture'
        user_portal = 'User Portal'

    class ManagementType:
        unassigned = 'Unassigned'
        monitoring = 'Monitoring'
        enrollment = 'Enrollment'
        provisioning = 'Provisioning'

    class RevokeReason:
        none = 0
        user_key_compromised = 1
        ca_key_compromised = 2
        user_changed_affiliation = 3
        certificate_superceded = 4
        original_use_no_longer_valid = 5


class CertificateClassNames:
    client_certificate_work = "Client Certificate Work"
    client_user_certificate_work = "Client User Certificate Work"
    server_certificate_work = "Server Certificate Work"
    x509_certificate = "X509 Certificate"

# endregion


# region Certificate Authority
class _CertificateAuthorityAttributesBase:
    additional_field = "Additional Field"
    concurrent_connection_limit = "Concurrent Connection Limit"
    contact = "Contact"
    created_by = "Created By"
    credential = "Credential"
    credits = "Credits"
    credits_alert = "Credits Alert"
    credits_used = "Credits Used"
    description = "Description"
    disabled = "Disabled"
    driver_arguments = "Driver Arguments"
    driver_name = "Driver Name"
    enhanced_key_usage = "Enhanced Key Usage"
    escalation_contact = "Escalation Contact"
    guid = "GUID"
    host = "Host"
    managed_by = "Managed By"
    manual_approval = "Manual Approval"
    metadata = "Metadata"
    port = "Port"
    protection_key = "Protection Key"
    rank = "Rank"
    reference = "Reference"
    renewal_window = "Renewal Window"
    retry_count = "Retry Count"
    retry_interval = "Retry Interval"
    san_enabled = "SAN Enabled"
    signature_algorithm = "Signature Algorithm"
    specific_end_date_enabled = "Specific End Date Enabled"
    template = "Template"
    test_account = "Test Account"
    timeout = "Timeout"
    validity_period = "Validity Period"
    vault_id = "Vault Id"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class CertificateAuthorityAttributes(_CertificateAuthorityAttributesBase):
    class Adaptable:
        allow_reissue = "Allow Reissue"
        certificate_credential = "Certificate Credential"
        connection_valid = "Connection Valid"
        custom_fields = "Custom Fields"
        interoperability_script = "Interoperability Script"
        log_debug = "Log Debug"
        powershell_script_hash_vault_id = "PowerShell Script Hash Vault Id"
        renewal_window = "Renewal Window"
        retry_after_script_hash_mismatch = "Retry After Script Hash Mismatch"
        secondary_credential = "Secondary Credential"

    class ComodoCCM:
        address = "Address"
        company_number = "Company Number"
        customer_login_uri = "Customer Login URI"
        domain_control_validation = "Domain Control Validation"
        domain_control_validation_email = "Domain Control Validation Email"
        organization = "Organization"
        postal_code = "Postal Code"
        secret_key = "Secret Key"
        uri = "URI"

    class Digicert:
        account_number = "Account Number"
        account_organization = "Account Organization"
        allow_reissue = "Allow Reissue"
        api_credentials = "API Credentials"
        api_key = "API Key"
        certificate_transparency = "Certificate Transparency"
        ev_allowed = "EV Allowed"
        ev_enabled = "EV Enabled"
        manual_approval = "Manual Approval"
        organizational_unit = "Organizational Unit"
        profile_id = "Profile ID"
        renewal_window = "Renewal Window"
        san_enabled = "SAN Enabled"
        uc_allowed = "UC Allowed"
        wildcard_allowed = "Wildcard Allowed"

    class EntrustCertificateServicesBase:
        certificate_type = "Certificate Type"
        create_entrust_user = "Create Entrust User"
        enrollment_server_for_web_folder = "Enrollment Server for Web Folder"
        epf_credential = "EPF Credential"
        epf_credential_dn = "EPF Credential DN"
        ini_file = "INI File"
        role = "Role"
        searchbase = "Searchbase"
        user_class_name = "User Class Name"

    class GeoTrustReseller:
        account_type = "Account Type"
        address = "Address"
        billing_contact_first_name = "Billing Contact First Name"
        billing_contact_internet_email_address = "Billing Contact Internet EMail Address"
        billing_contact_last_name = "Billing Contact Last Name"
        billing_contact_telephone_number = "Billing Contact Telephone Number"
        city = "City"
        country = "Country"
        interval = "Interval"
        organization = "Organization"
        partner_code = "Partner Code"
        postal_code = "Postal Code"
        state = "State"
        technical_contact_address = "Technical Contact Address"
        technical_contact_city = "Technical Contact City"
        technical_contact_country = "Technical Contact Country"
        technical_contact_first_name = "Technical Contact First Name"
        technical_contact_internet_email_address = "Technical Contact Internet EMail Address"
        technical_contact_last_name = "Technical Contact Last Name"
        technical_contact_organization = "Technical Contact Organization"
        technical_contact_postal_code = "Technical Contact Postal Code"
        technical_contact_state = "Technical Contact State"
        technical_contact_telephone_number = "Technical Contact Telephone Number"
        technical_contact_title = "Technical Contact Title"
        telephone_number = "Telephone Number"
        test_account = "Test Account"
        web_service_url = "Web Service URL"

    class GlobalSignMSSL:
        domain_id = "Domain ID"
        profile_id = "Profile ID"
        san_type = "SAN Type"
        web_service_url = "Web Service URL"

    class HydrantID:
        account_name = "Account Name"
        account_organization = "Account Organization"
        api_credentials = "API Credentials"
        certificate_type = "Certificate Type"
        subscriber_email = "Subscriber Email"
        ui_credentials = "UI Credentials"
        web_service_url = "Web Service URL"
        web_ui_url = "Web UI URL"

    class MSCA:
        enrollment_agent_certificate = "Enrollment Agent Certificate"
        given_name = "Given Name"
        include_cn_as_san = "Include CN as SAN"

    class OpenSSL:
        certificate_directory = "Certificate Directory"
        certificate_file = "Certificate File"
        configuration_file = "Configuration File"
        copy_extensions = "Copy Extensions"
        private_key_file = "Private Key File"
        private_key_password_credential = "Private Key Password Credential"
        temp_directory = "Temp Directory"

    class OpenTrust:
        connector_type = "Connector Type"
        fields = "Fields"
        retrieval_period = "Retrieval Period"
        web_service_url = "Web Service URL"

    class QuoVadis:
        account_name = "Account Name"
        account_organization = "Account Organization"
        api_credentials = "API Credentials"
        certificate_type = "Certificate Type"
        subscriber_email = "Subscriber Email"
        ui_credentials = "UI Credentials"
        web_service_url = "Web Service URL"
        web_ui_url = "Web UI URL"

    class RedHat:
        agent_port = "Agent Port"
        agent_url_surffix = "Agent URL Surffix"
        end_entity_port = "End Entity Port"
        end_entity_url_surffix = "End Entity URL Surffix"
        use_profile = "Use Profile"

    class RSA:
        ca_md5 = "CA MD5"
        ca_name = "CA Name"
        certificate_block = "Certificate Block"
        jurisdiction_id = "Jurisdiction ID"
        jurisdiction_name = "Jurisdiction Name"
        supported_validity_periods = "Supported Validity Periods"

    class SelfSigned:
        algorithm = "Algorithm"
        enhanced_key_usage = "Enhanced Key Usage"
        key_usage = "Key Usage"

    class Symantec:
        fields = "Fields"
        uri = "URI"

    class Thawte:
        certificate_block = "Certificate Block"
        certificate_transparency = "Certificate Transparency"
        retrieval_period = "Retrieval Period"
        server_type = "Server Type"
        signature_algorithm = "Signature Algorithm"
        uri = "URI"

    class TrustWave:
        interval = "Interval"
        reseller_id = "Reseller ID"
        retrieval_period = "Retrieval Period"
        web_service_url = "Web Service URL"

    class UniCERT:
        ca_dn = "CA DN"
        ra_dn = "RA DN"
        secure = "Secure"
        web_instance = "Web Instance"


class CertificateAuthorityClassNames:
    adaptable_ca = "Adaptable CA"
    comodo_ccm = "Comodo CCM"
    entrust_security_manager_ca = "Entrust Security Manager CA"
    geotrust_true_flex_ca = "GeotrustTrueFlex CA"
    http_ca_base = "HTTP CA Base"
    microsoft_ca = "Microsoft CA"
    microsoft_ca_pool = "Microsoft CA Pool"
    open_ssl_ca = "OpenSSL CA"
    redhat_ca = "Redhat CA"
    rsa_keon_ca = "RSA Keon CA"
    self_signed_ca = "Self Signed CA"
    symantec_lhk_ca = "Symantec LHK CA"
    unicert_ca = "UniCERT CA"
    verisign_ca = "VeriSign CA"
    verizon_ca = "Verizon CA"
    xolphin_ca = "Xolphin CA"
    zos_ca = "zOS CA"

# endregion


# region Certificate Trust Store
class CertificateTrustStoreClassNames:
    blue_coat_sslva_trust_store = "BlueCoat SSLVA Trust Store"
    capi_trust_store = "CAPI Trust Store"
    connect_direct_trust_store = "ConnectDirect Trust Store"
    f5_ltm_advanced_trust_store = "F5 LTM Advanced Trust Store"
    gsk_trust_store = "GSK Trust Store"
    jks_trust_store = "JKS Trust Store"
    palo_alto_network_fw_trust_store = "Palo Alto Network FW Trust Store"
    pem_trust_store = "PEM Trust Store"
    pkcs_12_trust_store = "PKCS#12 Trust Store"

# endregion


# region Cloud Instance Monitoring
class CloudInstanceMonitoringClassNames:
    aws_ec2_instance_monitor = 'AWS EC2 Instance Monitor'

# endregion


# region Credential
class _CredentialAttributesBase:
    contact = "Contact"
    created_by = "Created By"
    description = "Description"
    disabled = "Disabled"
    escalation_contact = "Escalation Contact"
    escalation_notice_interval = "Escalation Notice Interval"
    escalation_notice_start = "Escalation Notice Start"
    expiration = "Expiration"
    expiration_notice_interval = "Expiration Notice Interval"
    expiration_notice_start = "Expiration Notice Start"
    guid = "GUID"
    last_notification = "Last Notification"
    managed_by = "Managed By"
    metadata = "Metadata"
    protection_key = "Protection Key"
    reference = "Reference"
    shared = "Shared"
    vault_id = "Vault Id"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class CredentialAttributes(_CredentialAttributesBase):
    class Amazon:
        authentication_credential = "Authentication Credential"
        authentication_source = "Authentication Source"
        region_code = "Region Code"
        role = "Role"
        web_service_url = "Web Service URL"

    class Certificate:
        certificate = 'Certificate'
        username = 'Username'

    class CyberArkPassword:
        account_name = "Account Name"
        application_id = "Application ID"
        folder = "Folder"
        safe = "Safe"

    class CyberArkUsernamePassword:
        account_name = "Account Name"
        application_id = "Application ID"
        folder = "Folder"
        safe = "Safe"
        username = "Username"

    class Generic:
        pass

    class Password(_CredentialAttributesBase):
        pass

    class PrivateKey(_CredentialAttributesBase):
        username = 'Username'

    class UsernamePassword(_CredentialAttributesBase):
        username = 'Username'


class CredentialClassNames:
    amazon_credential = "Amazon Credential"
    automatic_password_credential = "Automatic Password Credential"
    certificate_credential = "Certificate Credential"
    generational_credential = "Generational Credential"
    generic_credential = "Generic Credential"
    password_credential = "Password Credential"
    private_key_credential = "Private Key Credential"
    username_password_credential = "Username Password Credential"

# endregion


# region Custom Field
class _CustomFieldAttributes:
    allowed_values = "Allowed Values"
    associated_classes = "Associated Classes"
    category = "Category"
    contact = "Contact"
    created_by = "Created By"
    default_values = "Default Values"
    description = "Description"
    disabled = "Disabled"
    escalation_contact = "Escalation Contact"
    guid = "GUID"
    help_text = "Help Text"
    label_text = "Label Text"
    localization = "Localization"
    managed_by = "Managed By"
    mandatory = "Mandatory"
    metadata = "Metadata"
    not_before = "Not Before"
    policyable = "Policyable"
    reference = "Reference"
    render_hidden = "Render Hidden"
    render_read_only = "Render Read Only"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class CustomFieldAttributes(_CustomFieldAttributes):
    class Choice:
        single = "Single"

    class DateTime:
        date_only = "Date Only"

    class Identity:
        single = "Single"

    class List:
        single = "Single"

    class Text:
        allowed_characters = "Allowed Characters"
        error_message = "Error Message"
        mask = "Mask"
        maximum_length = "Maximum Length"
        minimum_length = "Minimum Length"
        regular_expression = "Regular Expression"


class CustomFieldAttributeValues:
    class Type:
        text_string = 1
        list = 2
        date_time = 4
        identity = 5

# endregion


# region Device
class _DeviceAttributesBase:
    agentless_discovery_stage = "Agentless Discovery Stage"
    agentless_discovery_status = "Agentless Discovery Status"
    algorithm = "Algorithm"
    allow_agentless_discovery_and_remediation = "Allow Agentless Discovery and Remediation"
    allow_duplicate_private_keys = "Allow Duplicate Private Keys"
    allow_from = "Allow From"
    allow_multiple_authorized_keys = "Allow Multiple Authorized Keys"
    allow_root_access = "Allow Root Access"
    allow_shared_server_accounts = "Allow Shared Server Accounts"
    allow_ssh1 = "Allow Ssh1"
    allow_unencrypted_private_keys = "Allow Unencrypted Private Keys"
    allowed_algorithm = "Allowed Algorithm"
    allowed_command = "Allowed Command"
    allowed_vendor_types = "Allowed Vendor Types"
    approver = "Approver"
    automatic_rotation_cleanup_wait = "Automatic Rotation Cleanup Wait"
    automatic_rotation_enabled = "Automatic Rotation Enabled"
    automatic_rotation_interval = "Automatic Rotation Interval"
    automatic_rotation_lead_time = "Automatic Rotation Lead Time"
    bulk_provisioning_dn = "Bulk Provisioning Dn"
    bulk_provisioning_stage = "Bulk Provisioning Stage"
    bulk_provisioning_status = "Bulk Provisioning Status"
    client_id = "Client ID"
    client_machine_id = "Client Machine ID"
    cloud_instance_id = "Cloud Instance ID"
    cloud_region = "Cloud Region"
    cloud_service = "Cloud Service"
    concurrent_connection_limit = "Concurrent Connection Limit"
    connection_method = "Connection Method"
    contact = "Contact"
    created_by = "Created By"
    credential = "Credential"
    deny_from = "Deny From"
    deny_multiple_authentication_failures = "Deny Multiple Authentication Failures"
    description = "Description"
    disabled = "Disabled"
    disabled_on = "Disabled On"
    discovered_by_dn = "Discovered By DN"
    enforce_known_host = "Enforce Known Host"
    environment = "Environment"
    escalation_contact = "Escalation Contact"
    file_validation_error = "File Validation Error"
    file_validation_result = "File Validation Result"
    global_sudo = "Global sudo"
    guid = "GUID"
    host = "Host"
    host_trusts = "Host Trusts"
    jump_server_dn = "Jump Server DN"
    key_bit_strength = "Key Bit Strength"
    known_hosts = "Known Hosts"
    last_attempt_to_get_client_subsystem_record = "Last Attempt To Get Client Subsystem Record"
    last_discovery_date = "Last Discovery Date"
    last_discovery_planned = "Last Discovery Planned"
    last_known_fingerprint = "Last Known Fingerprint"
    last_known_key_type = "Last Known Key Type"
    last_validation = "Last Validation"
    last_validation_result = "Last Validation Result"
    location = "Location"
    managed_by = "Managed By"
    management_type = "Management Type"
    manual_approval = "Manual Approval"
    maximum_key_age = "Maximum Key Age"
    metadata = "Metadata"
    minimum_key_bit_strength = "Minimum Key Bit Strength"
    onboard_discovery_dn = "Onboard Discovery Dn"
    onboard_discovery_stage = "Onboard Discovery Stage"
    onboard_discovery_status = "Onboard Discovery Status"
    onboard_discovery_to_do = "Onboard Discovery To Do"
    placement_job_dn = "Placement Job Dn"
    port = "Port"
    previous_connection_credential_hash = "Previous Connection Credential Hash"
    privilege_elevation_command = "Privilege Elevation Command"
    protection_key = "Protection Key"
    reference = "Reference"
    remote_server_type = "Remote Server Type"
    required_options = "Required Options"
    required_sync_confirmation = "Required Sync Confirmation"
    root_server_access = "Root Server Access"
    secondary_credential = "Secondary Credential"
    server_access = "Server Access"
    ssh_device_status = "Ssh Device Status"
    ssh_device_type = "Ssh Device Type"
    ssh_key_encryption = "SSH Key Encryption"
    ssl_listen_host = "SSL Listen Host"
    ssl_listen_port = "SSL Listen Port"
    status = "Status"
    sudo_password_delay = "Sudo Password Delay"
    system_owned_keys = "System Owned Keys"
    temp_directory = "Temp Directory"
    terminal_columns = "Terminal Columns"
    terminal_rows = "Terminal Rows"
    terminal_type = "Terminal Type"
    timeout = "Timeout"
    trusted_fingerprint = "Trusted Fingerprint"
    trusted_key_type = "Trusted Key Type"
    trusted_root_users = "Trusted Root Users"
    trusted_users = "Trusted Users"
    update_cache = "Update Cache"
    use_specified_host = "Use Specified Host"
    validation_disabled = "Validation Disabled"
    validation_errors = "Validation Errors"
    validation_results = "Validation Results"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class DeviceAttributes(_DeviceAttributesBase):
    class DeviceBase:
        pass

    class JumpServer:
        consumers = "Consumers"
        location = "Location"
        ssh_connection_string = "SSH Connection String"
        ssh_version = "SSH Version"


class DevicesClassNames:
    device = 'Device'
    jump_server = 'Jump Server'

# endregion


# region Folder
class FolderClassNames:
    policy = 'Policy'


class FolderAttributes:
    certificate_origin = "Certificate Origin"
    contact = "Contact"
    created_by = "Created By"
    description = "Description"
    disabled = "Disabled"
    escalation_contact = "Escalation Contact"
    guid = "GUID"
    log_view_server = "Log View Server"
    managed_by = "Managed By"
    master_preferences = "Master Preferences"
    metadata = "Metadata"
    reference = "Reference"
    scep_ca_ident = "Scep CA Ident"
    scep_certificate_authority = "Scep Certificate Authority"
    scep_challenge_password = "Scep Challenge Password"
    scep_encryption_ra_certificate = "Scep Encryption RA Certificate"
    scep_intune_application_id = "Scep Intune Application Id"
    scep_intune_application_secret = "Scep Intune Application Secret"
    scep_intune_tenant_name = "Scep Intune Tenant Name"
    scep_ra_certificate = "Scep RA Certificate"
    scep_selection_rule = "Scep Selection Rule"
    scep_signing_ra_certificate = "Scep Signing RA Certificate"
    workflow = "Workflow"
    workflow_block = "Workflow Block"

# endregion


# region Identity
class IdentityClassNames:
    user = 'USER'
    security_group = 'GROUP'


class IdentityAttributes:
    class Types:
        user = 1
        security_group = 2
        distribution_group = 8

# endregion


# region Workflow
class _WorkflowAttributes:
    contact = "Contact"
    created_by = "Created By"
    description = "Description"
    disabled = "Disabled"
    escalation_contact = "Escalation Contact"
    guid = "GUID"
    managed_by = "Managed By"
    metadata = "Metadata"
    reference = "Reference"
    rule = "Rule"
    rule_vault_id = "Rule Vault Id"
    workflow = "Workflow"
    workflow_block = "Workflow Block"


class WorkflowAttributes(_WorkflowAttributes):
    class Adaptable:
        adaptable_workflow_text_field_1 = "Adaptable Workflow Text Field 1"
        adaptable_workflow_text_field_10 = "Adaptable Workflow Text Field 10"
        adaptable_workflow_text_field_11 = "Adaptable Workflow Text Field 11"
        adaptable_workflow_text_field_12 = "Adaptable Workflow Text Field 12"
        adaptable_workflow_text_field_2 = "Adaptable Workflow Text Field 2"
        adaptable_workflow_text_field_3 = "Adaptable Workflow Text Field 3"
        adaptable_workflow_text_field_4 = "Adaptable Workflow Text Field 4"
        adaptable_workflow_text_field_5 = "Adaptable Workflow Text Field 5"
        adaptable_workflow_text_field_6 = "Adaptable Workflow Text Field 6"
        adaptable_workflow_text_field_7 = "Adaptable Workflow Text Field 7"
        adaptable_workflow_text_field_8 = "Adaptable Workflow Text Field 8"
        adaptable_workflow_text_field_9 = "Adaptable Workflow Text Field 9"
        credential = "Credential"
        log_debug = "Log Debug"
        powershell_script = "PowerShell Script"
        powershell_script_hash_vault_id = "PowerShell Script Hash Vault Id"
        secondary_credential = "Secondary Credential"
        service_address = "Service Address"

    class Standard:
        approval_explanation = "Approval Explanation"
        approval_from = "Approval From"
        approval_reason = "Approval Reason"
        approver_not_found_timestamp = "Approver Not Found Timestamp"
        creation_date = "Creation Date"
        last_notification = "Last Notification"
        last_update = "Last Update"
        owner_object = "Owner Object"
        scheduled_start = "Scheduled Start"
        scheduled_stop = "Scheduled Stop"
        status = "Status"
        suspended_attribute = "Suspended Attribute"
        updated_by = "Updated By"
        user_data = "User Data"


class WorkflowAttributeValues:
    class Status:
        approved = 'Approved'
        approved_after = 'Approved After'
        approved_before = 'Approved Before'
        approved_between = 'Approved Between'
        pending = 'Pending'
        rejected = 'Rejected'


class WorkflowClassNames:
    adaptable_workflow = 'Adaptable Workflow'
    workflow = 'Workflow'

# endregion