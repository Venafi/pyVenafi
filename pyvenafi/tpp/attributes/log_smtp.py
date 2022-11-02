from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes


class LogSMTPAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log SMTP"
    attachment_behavior = Attribute('Attachment Behavior', min_version='21.2')
    bcc = Attribute('BCC', min_version='22.2')
    cc = Attribute('CC')
    host = Attribute('Host')
    item_vault_id = Attribute('Item Vault Id')
    log_delivery = Attribute('Log Delivery')
    message_body = Attribute('Message Body')
    recipient = Attribute('Recipient')
    smtp_credentials = Attribute('SMTP Credentials')
    secure = Attribute('Secure')
    sender = Attribute('Sender')
    subject = Attribute('Subject')
    template_vault_id = Attribute('Template Vault Id')
