from pytpp.tools.importer import Importer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytpp.api.authenticate import Authenticate
    from pytpp.properties.oauth import Scope
    from pytpp.features.definitions.features import Features
    from pytpp.features.definitions.attributes import Attributes
    from pytpp.features.definitions.attribute_names import AttributeNames
    from pytpp.features.definitions.attribute_values import AttributeValues
    from pytpp.features.definitions.classes import Classes
    from pytpp.logger import logger
    from pytpp import vtypes as Types

__getattr__ = Importer(name=__name__, imports={
    'Authenticate'   : ('pytpp.api', 'Authenticate'),
    'Scope'          : ('pytpp.properties.oauth', 'Scope'),
    'Features'       : ('pytpp.features.definitions.features', 'Features'),
    'Attributes'     : ('pytpp.features.definitions.attributes', 'Attributes'),
    'AttributeNames' : ('pytpp.features.definitions.attribute_names', 'AttributeNames'),
    'AttributeValues': ('pytpp.features.definitions.attribute_values', 'AttributeValues'),
    'Classes'        : ('pytpp.features.definitions.classes', 'Classes'),
    'logger'         : ('pytpp.logger', 'logger'),
    'Types'          : ('pytpp', 'vtypes'),
}).getattr
