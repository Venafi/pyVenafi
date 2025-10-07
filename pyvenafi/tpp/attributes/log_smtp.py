from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogSMTPAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log SMTP"
    attachment_behavior = Attribute('Attachment Behavior', min_version='21.4')
    bcc = Attribute('BCC', min_version='22.2')
    cc = Attribute('CC', min_version='21.4')
    component_vault_id = Attribute('Component Vault Id', min_version='23.3')
    factory_vault_id = Attribute('Factory Vault Id', min_version='23.3')
    host = Attribute('Host', min_version='21.4')
    item_vault_id = Attribute('Item Vault Id', min_version='21.4')
    log_delivery = Attribute('Log Delivery', min_version='21.4')
    message_body = Attribute('Message Body', min_version='21.4')
    no_html = Attribute('No Html', min_version='23.3')
    recipient = Attribute('Recipient', min_version='21.4')
    smtp_credentials = Attribute('SMTP Credentials', min_version='21.4')
    secure = Attribute('Secure', min_version='21.4')
    sender = Attribute('Sender', min_version='21.4')
    subject = Attribute('Subject', min_version='21.4')
    template_vault_id = Attribute('Template Vault Id', min_version='21.4')
