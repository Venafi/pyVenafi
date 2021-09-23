from pytpp.tools.importer import Importer
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.api.authenticate import Authenticate
    from pytpp.properties.oauth import Scope
    from pytpp.features import Features, AttributeNames, AttributeValues, Classes
    from pytpp.logger import logger
    from pytpp import vtypes as Types

__getattr__ = Importer(name=__name__, imports={
    'Authenticate'   : ('pytpp.api', 'Authenticate'),
    'Scope'          : ('pytpp.properties.oauth', 'Scope'),
    'Features'       : ('pytpp.features', 'Features'),
    'AttributeNames' : ('pytpp.features', 'AttributeNames'),
    'AttributeValues': ('pytpp.features', 'AttributeValues'),
    'Classes'        : ('pytpp.features', 'Classes'),
    'logger'         : ('pytpp.logger', 'logger'),
    'Types'          : ('pytpp', 'vtypes'),
}).getattr
