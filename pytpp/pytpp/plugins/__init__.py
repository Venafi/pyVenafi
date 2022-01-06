from pytpp.plugins.api.authenticate import Authenticate
from pytpp.plugins.features.definitions.features import Features
# noinspection PyUnresolvedReferences
from pytpp.properties.oauth import Scope
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attributes import Attributes
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.classes import Classes as ClassNames
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.legacy_classes import Classes as __C
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
# noinspection PyUnresolvedReferences
from pytpp.tools.logger import logger
# noinspection PyUnresolvedReferences
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
