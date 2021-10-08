from pytpp.tools.importer import Importer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytpp.plugins.api.authenticate import Authenticate, Aperture
    # noinspection PyUnresolvedReferences
    from pytpp.properties.oauth import Scope
    # noinspection PyUnresolvedReferences
    from pytpp.plugins.features import Features, AttributeNames, AttributeValues, Classes
    # noinspection PyUnresolvedReferences
    from pytpp.logger import logger
    # noinspection PyUnresolvedReferences
    from pytpp import vtypes as Types

__getattr__ = Importer(name=__name__, imports={
    'Authenticate'   : ('pytpp.plugins.api.authenticate', 'Authenticate'),
    'Aperture'       : ('pytpp.plugins.api.authenticate', 'Authenticate'),
    'Scope'          : ('pytpp.properties.oauth', 'Scope'),
    'Features'       : ('pytpp.plugins.features', 'Features'),
    'AttributeNames' : ('pytpp.plugins.features', 'AttributeNames'),
    'AttributeValues': ('pytpp.plugins.features', 'AttributeValues'),
    'Classes'        : ('pytpp.plugins.features', 'Classes'),
    'logger'         : ('pytpp.logger', 'logger'),
    'Types'          : ('pytpp', 'vtypes'),
}).getattr
