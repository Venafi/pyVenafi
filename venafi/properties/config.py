class _ApplicationAttributes:
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
    file_owner__group = "File Owner: Group"
    file_owner__user = "File Owner: User"
    file_permissions__group = "File Permissions: Group"
    file_permissions__user = "File Permissions: User"
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


class ApplicationAttributes:
    class Apache(_ApplicationAttributes):
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

    class PKCS11(_ApplicationAttributes):
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


class _ApplicationAttributeValues:
    class ConnectionMethod:
        ssh = 'SSH'
        winrm = 'WinRM'
        winrms = 'WinRMs'

    class ProtectionType:
        module = 'Module'
        ocs = 'OCS'
        softcard = 'softcard'


class ApplicationAttributeValues:
    class PKCS11(_ApplicationAttributeValues):
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


################################


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


class CertificateClassNames:
    client_certificate_work = "Client Certificate Work"
    client_user_certificate_work = "Client User Certificate Work"
    server_certificate_work = "Server Certificate Work"
    x509_certificate = "X509 Certificate"


################################


class _CertificateAuthorityAttributes:
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


class CertificateAuthorityAttributes:
    class SelfSigned(_CertificateAuthorityAttributes):
        algorithm = "Algorithm"
        enhanced_key_usage = "Enhanced Key Usage"
        key_usage = "Key Usage"

    class MSCA(_CertificateAuthorityAttributes):
        enrollment_agent_certificate = "Enrollment Agent Certificate"
        given_name = "Given Name"
        include_cn_as_san = "Include CN as SAN"


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


################################


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


################################


class CloudInstanceMonitoringClassNames:
    aws_ec2_instance_monitor = 'AWS EC2 Instance Monitor'


################################


class _CredentialAttributes:
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


class CredentialAttributes:
    class Amazon(_CredentialAttributes):
        authentication_credential = "Authentication Credential"
        authentication_source = "Authentication Source"
        region_code = "Region Code"
        role = "Role"
        web_service_url = "Web Service URL"

    class Certificate(_CredentialAttributes):
        certificate = 'Certificate'
        username = 'Username'

    class CyberArkPassword(_CredentialAttributes):
        account_name = "Account Name"
        application_id = "Application ID"
        folder = "Folder"
        safe = "Safe"

    class CyberArkUsernamePassword(_CredentialAttributes):
        account_name = "Account Name"
        application_id = "Application ID"
        folder = "Folder"
        safe = "Safe"
        username = "Username"

    class Generic(_CredentialAttributes):
        pass

    class Password(_CredentialAttributes):
        pass

    class PrivateKey(_CredentialAttributes):
        username = 'Username'

    class UsernamePassword(_CredentialAttributes):
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


################################


class _DeviceAttributes:
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


class DeviceAttributes:
    class Device(_DeviceAttributes):
        pass

    class JumpServer(_DeviceAttributes):
        consumers = "Consumers"
        location = "Location"
        ssh_connection_string = "SSH Connection String"
        ssh_version = "SSH Version"


class DevicesClassNames:
    device = 'Device'
    jump_server = 'Jump Server'


################################


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


################################


class WorkflowClassNames:
    workflow = 'Workflow'