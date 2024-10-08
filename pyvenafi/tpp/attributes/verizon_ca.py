from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from pyvenafi.tpp.attributes.proxy import ProxyAttributes

class VerizonCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "Verizon CA"
    admin_email = Attribute('Admin Email')
    admin_firstname = Attribute('Admin Firstname')
    admin_surname = Attribute('Admin Surname')
    admin_telnumber = Attribute('Admin Telnumber')
    certificate_block = Attribute('Certificate Block')
