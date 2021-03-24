from typing import List, Dict
from venafi.tools.helpers.date_converter import from_date_string


class CertificateDetails:
    def __init__(self, response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        self.allowed_app_type = response_object.get('allowedAppType')  # type: str
        self.aperture_status = response_object.get('apertureStatus')  # type: List[str]
        self.approver = response_object.get('approver')  # type: List[str]
        self.city = response_object.get('city')  # type: str
        self.common_name = response_object.get('commonName')  # type: str
        self.contact = response_object.get('contact')  # type: List[str]
        self.country = response_object.get('country')  # type: str
        self.days_to_expire = response_object.get('daysToExpire')  # type: int
        self.description = response_object.get('description')  # type: str
        self.dn = response_object.get('dn')  # type: str
        self.dns_sans = response_object.get('dnsSans')  # type: List[str]
        self.domain = response_object.get('domain')  # type: str
        self.elliptic_curve = response_object.get('ellipticCurve')  # type: str
        self.email_sans = response_object.get('emailSans')  # type: List[str]
        self.error_details = response_object.get('errorDetails')  # type: str
        self.id = response_object.get('id')  # type: str
        self.installations = response_object.get('installations')  # type: int
        self.ip_sans = response_object.get('ipSans')  # type: List[str]
        self.is_disabled = response_object.get('isDisabled')  # type: bool
        self.is_in_error = response_object.get('isInError')  # type: bool
        self.is_rename_allowed = response_object.get('isRenameAllowed')  # type: bool
        self.is_validation_enabled = response_object.get('isValidationEnabled')  # type: bool
        self.issuer = response_object.get('issuer')  # type: str
        self.key_algorithm = response_object.get('keyAlgorithm')  # type: str
        self.key_size = response_object.get('keySize')  # type: int
        self.last_renewed_by = response_object.get('lastRenewedBy')  # type: List[str]
        self.management_type = response_object.get('managementType')  # type: str
        self.name = response_object.get('name')  # type: str
        self.organization = response_object.get('organization')  # type: str
        self.organizational_unit = response_object.get('organizationalUnit')  # type: List[str]
        self.parent_dn = response_object.get('parentDn')  # type: str
        self.renewal_date = from_date_string(response_object.get('renewalDate'))
        self.revocation_status = response_object.get('revocationStatus')  # type: str
        self.risks = response_object.get('risks')  # type: List[str]
        self.serial_number = response_object.get('serialNumber')  # type: str
        self.signature_algorithm = response_object.get('signatureAlgorithm')  # type: str
        self.single_click_actions = response_object.get('singleClickActions')  # type: List[str]
        self.state = response_object.get('state')  # type: str
        self.status_details = response_object.get('statusDetails')  # type: Dict[str, List[str]]
        self.tls_endpoints = response_object.get('tlsEndpoints')  # type: int
        self.trust_net_reputation_score = response_object.get('trustNetReputationScore')  # type: int
        self.trust_net_reviewed_by = response_object.get('trustNetReviewedBy')  # type: str
        self.trust_net_reviewed_date = from_date_string(response_object.get('trustNetReviewedDate'))
        self.upn_sans = response_object.get('upnSans')  # type: List[str]
        self.uri_sans = response_object.get('uriSans')  # type: List[str]
        self.usage = response_object.get('usage')  # type: str
        self.use_manual_csr = response_object.get('useManualCsr')  # type: bool
        self.valid_from = from_date_string(response_object.get('validFrom'))
        self.valid_to = from_date_string(response_object.get('validTo'))
        self.validation_state = response_object.get('validationState')  # type: str
        self.validity_period_days = response_object.get('validityPeriodDays')  # type: int
