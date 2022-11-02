from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.client_portal_base import ClientPortalBaseAttributes
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes
from pyvenafi.tpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ClientUserCertificateWorkAttributes(ClientPortalBaseAttributes, ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client User Certificate Work"
    certificate_bundle_capacity = Attribute('Certificate Bundle Capacity')
    certificate_bundle_capacity_mobile_config = Attribute('Certificate Bundle Capacity Mobile Config')
    certificate_container = Attribute('Certificate Container')
    certificate_icon = Attribute('Certificate Icon')
    download_instructions = Attribute('Download Instructions')
    download_limit = Attribute('Download Limit')
    include_historic_certificates = Attribute('Include Historic Certificates')
    membership_loss_disable = Attribute('Membership Loss Disable')
    membership_loss_revoke = Attribute('Membership Loss Revoke')
    naming_pattern = Attribute('Naming Pattern')
    outlook_profile_generation = Attribute('Outlook Profile Generation')
    outlook_profile_name = Attribute('Outlook Profile Name')
    outlook_profile_options = Attribute('Outlook Profile Options')
    portal_friendly_name = Attribute('Portal Friendly Name')
    publish_to_identity = Attribute('Publish To Identity')
    publish_to_identity_on_pre_enroll = Attribute('Publish To Identity on Pre-Enroll')
    required_member_identity = Attribute('Required Member Identity')
    transfer_allowed = Attribute('Transfer Allowed')
