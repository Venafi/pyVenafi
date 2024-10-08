from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class X509RootCertificateAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 Root Certificate"
    aia_ca_issuer_location_description = Attribute('AIA CA Issuer Location Description')
    aia_ca_issuer_location_disabled = Attribute('AIA CA Issuer Location Disabled')
    aia_ca_issuer_location_mode = Attribute('AIA CA Issuer Location Mode')
    aia_ca_issuer_location_rank = Attribute('AIA CA Issuer Location Rank')
    aia_ca_issuer_location_status = Attribute('AIA CA Issuer Location Status')
    aia_ca_issuer_publishing_location = Attribute('AIA CA Issuer Publishing Location')
    aia_ocsp_location_description = Attribute('AIA OCSP Location Description')
    aia_ocsp_location_disabled = Attribute('AIA OCSP Location Disabled')
    aia_ocsp_location_mode = Attribute('AIA OCSP Location Mode')
    aia_ocsp_location_rank = Attribute('AIA OCSP Location Rank')
    aia_ocsp_location_status = Attribute('AIA OCSP Location Status')
    aia_ocsp_publishing_location = Attribute('AIA OCSP Publishing Location')
    cdp_aia_actions = Attribute('CDP AIA Actions')
    cdp_aia_in_error = Attribute('CDP AIA In Error')
    cdp_aia_status = Attribute('CDP AIA Status')
    cdp_aia_verification_now = Attribute('CDP AIA Verification Now')
    cdp_crl_metadata = Attribute('CDP CRL Metadata')
    cdp_crl_next_publish_percentage = Attribute('CDP CRL Next Publish Percentage')
    cdp_location_description = Attribute('CDP Location Description')
    cdp_location_disabled = Attribute('CDP Location Disabled')
    cdp_location_mode = Attribute('CDP Location Mode')
    cdp_location_rank = Attribute('CDP Location Rank')
    cdp_location_status = Attribute('CDP Location Status')
    cdp_publishing_location = Attribute('CDP Publishing Location')
    crl_delta_number = Attribute('CRL Delta Number')
    crl_delta_publishing_location = Attribute('CRL Delta Publishing Location')
    crl_issuer_dn = Attribute('CRL Issuer DN')
    crl_issuer_identifier = Attribute('CRL Issuer Identifier')
    crl_next_publish_date = Attribute('CRL Next Publish Date')
    crl_next_update = Attribute('CRL Next Update')
    crl_number = Attribute('CRL Number')
    crl_this_update = Attribute('CRL This Update')
    certificate_vault_id = Attribute('Certificate Vault Id')
    discovered_on = Attribute('Discovered On')
    escalation_notice_interval = Attribute('Escalation Notice Interval')
    escalation_notice_start = Attribute('Escalation Notice Start')
    expiration_notice_interval = Attribute('Expiration Notice Interval')
    expiration_notice_start = Attribute('Expiration Notice Start')
    monitored_uri_verification_engine_info = Attribute('Monitored URI Verification Engine Info')
    monitored_uri_verification_last_check = Attribute('Monitored URI Verification Last Check')
    monitored_uri_verification_last_notification = Attribute('Monitored URI Verification Last Notification')
    monitored_uri_verification_run_identifier = Attribute('Monitored URI Verification Run Identifier')
    monitored_uri_verification_uri_identifier = Attribute('Monitored URI Verification URI Identifier')
    required_attribute_for_signing_certificate = Attribute('Required Attribute For Signing Certificate')
    required_attribute_for_time_stamping_certificate = Attribute('Required Attribute For Time Stamping Certificate')
    trust_for_signing = Attribute('Trust For Signing')
    trust_for_time_stamping = Attribute('Trust For Time Stamping')
    trusted_status = Attribute('Trusted Status')
