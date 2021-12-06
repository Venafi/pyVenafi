from warnings import warn
from pytpp.api.authenticate import Authenticate
from pytpp.properties.oauth import Scope
from pytpp.features.definitions.features import Features
from pytpp.features.definitions.attributes import Attributes
from pytpp.features.definitions.attribute_values import AttributeValues
from pytpp.features.definitions.classes import Classes as ClassNames
from pytpp.tools.logger import logger
from pytpp.tools import vtypes as Types
# Legacy imports
from pytpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
from pytpp.features.definitions.legacy_classes import Classes as __C

def __getattr__(name):
    attr = None
    if name == 'AttributeNames':
        attr = __AN
    elif name == 'Classes':
        attr = __C
    return attr

