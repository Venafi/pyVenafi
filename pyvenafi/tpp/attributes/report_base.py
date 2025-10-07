from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes

class ReportBaseAttributes(DriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report Base"
    csv_vault_id = Attribute('CSV Vault Id')
    configuration = Attribute('Configuration')
    creation_date = Attribute('Creation Date')
    credential = Attribute('Credential')
    delivery_type = Attribute('Delivery Type')
    enforce_known_host = Attribute('Enforce Known Host')
    format = Attribute('Format')
    html_vault_id = Attribute('HTML Vault Id')
    internet_email_address = Attribute('Internet EMail Address')
    last_known_fingerprint = Attribute('Last Known Fingerprint')
    last_known_key_type = Attribute('Last Known Key Type')
    last_run = Attribute('Last Run')
    options = Attribute('Options')
    pdf_vault_id = Attribute('PDF Vault Id')
    publishing_host = Attribute('Publishing Host')
    publishing_location = Attribute('Publishing Location')
    rtf_vault_id = Attribute('RTF Vault Id')
    report_template = Attribute('Report Template')
    skip_empty = Attribute('Skip Empty')
    title = Attribute('Title')
    trusted_fingerprint = Attribute('Trusted Fingerprint')
    trusted_key_type = Attribute('Trusted Key Type')
    xml_vault_id = Attribute('XML Vault Id')
