# noinspection PyUnresolvedReferences
from pytpp._about import (
    __version__, __author__, __author_email__, __project_name__,
    __project_url__,
)
# noinspection PyUnresolvedReferences
from pytpp.plugins.api.authenticate import Authenticate
# noinspection PyUnresolvedReferences
from pytpp.plugins.features.definitions.features import Features
# noinspection PyUnresolvedReferences
from pytpp.api.websdk.enums.oauth import Scope
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attributes import Attributes
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.classes import Classes as ClassNames
# noinspection ALL
from pytpp.features.definitions.legacy_classes import Classes as __C
# noinspection ALL
from pytpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
# noinspection PyUnresolvedReferences
from pytpp.tools.logger import logger, features_logger, api_logger
# noinspection ALL
from pytpp.tools import vtypes as Types
# Legacy imports
# noinspection ALL
from pytpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
# noinspection ALL
from pytpp.features.definitions.legacy_classes import Classes as __C


def __getattr__(name):
    if name == 'AttributeNames':
        return __AN
    elif name == 'Classes':
        return __C
    raise ImportError(f'{name} cannot be imported because it does not exist.')
