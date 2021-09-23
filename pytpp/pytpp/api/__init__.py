from pytpp.tools.importer import Importer
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.api.authenticate import Authenticate

__getattr__ = Importer(name=__name__, imports={
    'Authenticate': ('pytpp.api.authenticate', 'Authenticate'),
}).getattr
