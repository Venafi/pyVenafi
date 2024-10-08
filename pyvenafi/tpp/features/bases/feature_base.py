from __future__ import annotations

import logging
import os
import re
import time
from typing import (
    TYPE_CHECKING,
    Union,
)

from packaging.version import Version

from pyvenafi.logger import (
    features_logger,
    logger,
)
from pyvenafi.tpp.api.websdk.enums.secret_store import Namespaces
from pyvenafi.tpp.api.websdk.models import (
    config,
    identity as ident,
)
from pyvenafi.tpp.features.definitions.exceptions import (
    InvalidResultCode,
    ObjectDoesNotExist,
)

if TYPE_CHECKING:
    from pyvenafi.tpp.api.authenticate import Authenticate

def feature(name: str):
    def decorate(cls):
        if int(os.getenv('PYVENAFI_DOC_IN_PROGRESS', 0)):
            return cls
        setattr(cls, '__feature__', name)
        return features_logger.wrap_class(
            level=logging.DEBUG,
            exclude='_.*'
        )(cls)

    return decorate

class FeatureBase:
    def __init__(self, api: 'Authenticate'):
        self._api = api

    def _config_create(
        self, name: str, parent_folder_dn: str, config_class: str, attributes: dict = None,
        get_if_already_exists: bool = True
    ):
        if attributes:
            attributes = self._name_value_list(attributes=attributes)

        dn = f'{parent_folder_dn}\\{name}'
        response = self._api.websdk.Config.Create.post(
            object_dn=dn, class_name=str(config_class),
            name_attribute_list=attributes or []
        )
        result = response.result
        if result.code != 1:
            if result.code == 401 and get_if_already_exists:
                return self._get_config_object(object_dn=dn)
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

        return response.object

    def _config_delete(self, object_dn, recursive: bool = False):
        result = self._api.websdk.Config.Delete.post(object_dn=object_dn, recursive=recursive).result
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def _get_config_object(
        self, object_dn: str = None, object_guid: str = None,
        raise_error_if_not_exists: bool = True, valid_class_names: list[str] = None
    ):
        if not (object_dn or object_guid):
            raise ValueError(
                'Must supply either an Object DN or Object GUID, but neither was provided.'
            )
        if isinstance(object_dn, config.Object):
            obj = object_dn
        elif isinstance(object_guid, config.Object):
            obj = object_guid
        else:
            response = self._api.websdk.Config.IsValid.post(object_dn=object_dn, object_guid=object_guid)
            if response.result.code == 400:
                if raise_error_if_not_exists:
                    raise ObjectDoesNotExist(f'"{object_dn or object_guid}" does not exist.')
                obj = config.Object()
            else:
                obj = response.object
        if valid_class_names and obj.type_name not in valid_class_names:
            valid_class_names = "\n".join(f"*  {i}" for i in valid_class_names)
            raise TypeError(
                f'"{object_dn or object_guid}" exists, but is not the expected class type.\n'
                f'Got type "{obj.type_name}" instead of one of \n{valid_class_names}.'
            )
        return obj

    def _get_identity_object(
        self, prefixed_name: str = None, prefixed_universal: str = None,
        raise_error_if_not_exists: bool = True
    ):
        if not (prefixed_name or prefixed_universal):
            raise ValueError(
                'Must supply either an prefixed_name or prefixed_universal, but neither was provided.'
            )
        if isinstance(prefixed_name, ident.Identity):
            return prefixed_name
        if isinstance(prefixed_universal, ident.Identity):
            return prefixed_universal

        try:
            response = self._api.websdk.Identity.Validate.post(
                identity=self._identity_dict(prefixed_name=prefixed_name, prefixed_universal=prefixed_universal)
            )
            identity = response.identity if response.api_response.content else None
        except:
            identity = None

        if identity is not None:
            return identity
        elif not raise_error_if_not_exists:
            return ident.Identity()
        else:
            raise ObjectDoesNotExist(f'Could not find identity "{prefixed_name or prefixed_universal}".')

    @staticmethod
    def _identity_dict(prefixed_name: str = None, prefixed_universal: str = None):
        """
        Creates an ID object to write to the Identity APIs.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:
            {
                'PrefixedUniversal': ``prefixed_universal``,
                'PrefixedName': ``prefixed_name``
            }
        """
        d = {}
        if prefixed_name:
            d.update(
                {
                    'PrefixedName': prefixed_name
                }
            )
        if prefixed_universal:
            d.update(
                {
                    'PrefixedUniversal': prefixed_universal
                }
            )
        return d

    @staticmethod
    def _is_prefixed_universal(identity):
        if isinstance(identity, str):
            if ':' not in identity:
                return False
            prefix, identity = identity.split(':', maxsplit=1)
            regex = '^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$'
            return bool(re.match(pattern=regex, string=identity))
        return False

    @staticmethod
    def _is_obj_guid(obj: str):
        regex = '^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$'
        return isinstance(obj, str) and bool(re.match(pattern=regex, string=obj))

    def _get_prefixed_name(self, identity: 'Union[ident.Identity, str, None]'):
        if identity is None:
            return None
        if hasattr(identity, 'prefixed_name'):
            return identity.prefixed_name
        if self._is_prefixed_universal(identity):
            return self._get_identity_object(prefixed_universal=identity).prefixed_name
        return identity

    def _get_prefixed_universal(self, identity: 'Union[ident.Identity, str, None]'):
        if identity is None:
            return None
        if hasattr(identity, 'prefixed_universal'):
            return identity.prefixed_universal
        if self._is_prefixed_universal(identity):
            return identity
        return self._get_identity_object(prefixed_name=identity).prefixed_universal

    def _get_dn(self, obj: 'Union[config.Object, str, None]', parent_dn: str = None):
        if obj is None:
            return None
        if hasattr(obj, 'dn'):
            return obj.dn
        if self._is_obj_guid(obj):
            return self._get_config_object(object_guid=obj).dn
        if parent_dn and not obj.startswith(parent_dn):
            obj = parent_dn.rstrip('\\') + '\\' + obj.rstrip('\\')
        if not obj.startswith(r'\VED'):
            return '\\VED\\' + obj.strip("\\")
        else:
            return obj

    def _get_guid(self, obj: 'Union[config.Object, str, None]', parent_dn: str = None):
        if obj is None:
            return None
        if hasattr(obj, 'guid'):
            return obj.guid
        if self._is_obj_guid(obj):
            return obj
        if parent_dn and not obj.startswith(parent_dn):
            obj = parent_dn.rstrip('\\') + f'\\{obj}'
        if not obj.startswith(r'\VED'):
            obj = '\\VED\\' + obj.strip("\\")
        return self._get_config_object(object_dn=obj).guid

    @staticmethod
    def _log_warning_message(msg: str):
        features_logger.warning(msg, stacklevel=2)

    @staticmethod
    def __no_op(*args, **kwargs):
        pass

    # noinspection ALL
    @staticmethod
    def _name_type_value(name: str, type: str, value):
        return {
            'Name' : str(name),
            'Type' : str(type),
            'Value': str(value)
        }

    @staticmethod
    def _name_value_list(attributes: dict[str, list[str]]):
        nvl = []
        for n, v in attributes.items():
            if v is None:
                continue
            if not isinstance(v, (list, tuple, set)):
                v = str(v)
            else:
                v = list(map(str, v))
            nvl.append(config.NameAttribute(name=n, value=v))
        return nvl

    def _secret_store_delete(self, object_dn: str, namespace: str = Namespaces.config):
        result = self._api.websdk.SecretStore.OwnerDelete.post(namespace=namespace, owner=object_dn).result
        if result.code != 0:
            raise InvalidResultCode(code=result.code, code_description=result.secret_store_result)

    def _is_version_compatible(self, minimum: str = '', maximum: str = ''):
        if minimum and self._api._tpp_version <= Version(minimum):
            return False
        if maximum and self._api._tpp_version >= Version(maximum):
            return False
        return True

    class _Timeout:
        def __init__(self, timeout):
            self.timeout = timeout
            self.max_time = timeout + time.time()
            self._cm = logger.suppressed(999)

        def __enter__(self):
            self._cm.__enter__()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self._cm.__exit__(exc_type, exc_val, exc_tb)
            return

        def is_expired(self, poll: float = 0.5):
            if time.time() >= self.max_time:
                return True
            if poll:
                time.sleep(poll)

        @staticmethod
        def poll(seconds: float):
            time.sleep(seconds)
