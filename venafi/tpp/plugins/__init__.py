# noinspection PyUnresolvedReferences
from venafi.tpp._about import (
    __version__, __author__, __author_email__, __project_name__,
    __project_url__,
)
# noinspection PyUnresolvedReferences
from venafi.tpp.plugins.api.authenticate import Authenticate
# noinspection PyUnresolvedReferences
from venafi.tpp.plugins.features.definitions.features import Features
# noinspection PyUnresolvedReferences
from venafi.tpp.api.websdk.enums.oauth import Scope
# noinspection PyUnresolvedReferences
from venafi.tpp.features.definitions.attributes import Attributes
# noinspection PyUnresolvedReferences
from venafi.tpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from venafi.tpp.features.definitions.classes import Classes as ClassNames
# noinspection ALL
from venafi.tpp.features.definitions.legacy_classes import Classes as __C
# noinspection ALL
from venafi.tpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
# noinspection PyUnresolvedReferences
from venafi.logger import logger, features_logger, api_logger
# noinspection ALL
from venafi.tpp.tools import vtypes as Types
# Legacy imports
# noinspection ALL
from venafi.tpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
# noinspection ALL
from venafi.tpp.features.definitions.legacy_classes import Classes as __C


def __getattr__(name):
    if name == 'AttributeNames':
        return __AN
    elif name == 'Classes':
        return __C
    raise ImportError(f'{name} cannot be imported because it does not exist.')
