import inspect
import time
import os
import re
from pytpp.properties.response_objects.config import Config
from pytpp.properties.response_objects.identity import Identity
from pytpp.logger import logger, LogTags
from pytpp.properties.secret_store import Namespaces
from pytpp.api.authenticate import Authenticate
from typing import List, Dict, Union
from packaging.version import Version


def feature():
    def decorate(cls):
        if int(os.getenv('PYTPP_DOC_IN_PROGRESS', 0)):
            return cls
        for attr, fn in inspect.getmembers(cls, inspect.isroutine):
            # Only public methods are decorated.
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('_'):
                if type(cls.__dict__.get(fn.__name__)) in {staticmethod, classmethod}:
                    setattr(cls, attr, logger.wrap_func(
                        log_tag=LogTags.feature,
                        mask_input_regexes=['self', 'cls'],
                        is_static_or_classmethod=True
                    )(getattr(cls, attr)))
                else:
                    setattr(cls, attr, logger.wrap_func(
                        log_tag=LogTags.feature,
                        mask_input_regexes=['self', 'cls'],
                    )(getattr(cls, attr)))
        return cls

    return decorate


@feature()
class FeatureBase:
    def __init__(self, api: Authenticate):
        self._api = api

    def _config_create(self, name: str, parent_folder_dn: str, config_class: str, attributes: dict = None,
                       get_if_already_exists: bool = True, keep_list_values: bool = False):
        if attributes:
            attributes = self._name_value_list(attributes=attributes, keep_list_values=keep_list_values)

        dn = f'{parent_folder_dn}\\{name}'
        ca = self._api.websdk.Config.Create.post(object_dn=dn, class_name=config_class,
                                                 name_attribute_list=attributes or [])
        result = ca.result
        if result.code != 1:
            if result.code == 401 and get_if_already_exists:
                return self._get_config_object(object_dn=dn)
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return ca.object

    def _config_delete(self, object_dn, recursive: bool = False):
        result = self._api.websdk.Config.Delete.post(object_dn=object_dn, recursive=recursive).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def _get_config_object(self, object_dn: str = None, object_guid: str = None,
                           raise_error_if_not_exists: bool = True):
        if not (object_dn or object_guid):
            raise ValueError(
                'Must supply either an Object DN or Object GUID, but neither was provided.'
            )
        obj = self._api.websdk.Config.IsValid.post(object_dn=object_dn, object_guid=object_guid)
        if obj.result.code == 400 and not raise_error_if_not_exists:
            # The object doesn't exist, but just return an empty object.
            return Config.Object(response_object={})
        return obj.object

    def _get_identity_object(self, prefixed_name: str = None, prefixed_universal: str = None):
        identity = self._api.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name, prefixed_universal=prefixed_universal)
        ).identity

        return identity

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
            d.update({'PrefixedName': prefixed_name})
        if prefixed_universal:
            d.update({'PrefixedUniversal': prefixed_universal})
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

    def _get_prefixed_name(self, identity: Union[Identity.Identity, str]):
        if isinstance(identity, Identity.Identity):
            return identity.prefixed_name
        if self._is_prefixed_universal(identity):
            logger.log(f'Getting prefixed name from prefixed GUID: {identity}')
            return self._get_identity_object(prefixed_universal=identity).prefixed_name
        return identity

    def _get_prefixed_universal(self, identity: Union[Identity.Identity, str]):
        if isinstance(identity, Identity.Identity):
            return identity.prefixed_name
        if self._is_prefixed_universal(identity):
            return identity
        logger.log(f'Getting prefixed name from prefixed GUID: {identity}')
        return self._get_identity_object(prefixed_name=identity).prefixed_universal

    def _get_dn(self, obj: Union[Config.Object, str]):
        if isinstance(obj, Config.Object):
            return obj.dn
        if self._is_obj_guid(obj):
            logger.log(f'Getting DN from GUID: {obj}')
            return self._get_config_object(object_guid=obj).dn
        if not obj.startswith(r'\VED'):
            return '\\VED\\' + obj.strip("\\")
        else:
            return obj

    def _get_guid(self, obj: Union[Config.Object, str]):
        if isinstance(obj, Config.Object):
            return obj.guid
        if self._is_obj_guid(obj):
            return obj
        logger.log(f'Getting GUID from DN: {obj}')
        if not obj.startswith(r'\VED'):
            obj = '\\VED\\' + obj.strip("\\")
        return self._get_config_object(object_dn=obj).guid

    def _get_config_name(self, obj: Union[Config.Object, str]):
        if isinstance(obj, Config.Object):
            return obj.name
        if self._is_obj_guid(obj):
            return self._get_config_object(object_guid=obj).name
        if '\\' in obj:
            return obj.rsplit('\\', maxsplit=1)[-1]
        return obj

    @staticmethod
    def _log_warning_message(msg: str):
        logger.log(msg=msg, log_tag=LogTags.critical, num_prev_callers=2)

    @staticmethod
    def __no_op(*args, **kwargs):
        pass

    @staticmethod
    def _name_type_value(name: str, type: str, value):
        return {'Name': str(name), 'Type': str(type), 'Value': str(value)}

    @staticmethod
    def _name_value_list(attributes: Dict[str, List[str]], keep_list_values: bool = False):
        nvl = []
        for name, value in attributes.items():
            if value is None:
                continue
            elif isinstance(value, list):
                if keep_list_values is True:
                    nvl.append({'Name': str(name), 'Value': value})
                else:
                    for v in value:
                        nvl.append({'Name': str(name), 'Value': str(v)})
            elif not isinstance(value, dict):
                nvl.append({'Name': str(name), 'Value': str(value)})
        return nvl

    def _secret_store_delete(self, object_dn: str, namespace: str = Namespaces.config):
        owners = self._api.websdk.SecretStore.LookupByOwner.post(namespace=namespace, owner=object_dn)
        result = owners.result
        if result.code != 0:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

        for vault_id in owners.vault_ids:
            result = self._api.websdk.SecretStore.Delete.post(vault_id=vault_id).result
            if result.code != 0:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

    def _enforce_version(self, minimum: str = '', maximum: str = ''):
        if minimum and self._api._version < Version(minimum):
            raise ValueError(f'Incompatible version. This feature requires at least TPP {minimum}.')
        if maximum and self._api._version > Version(maximum):
            raise ValueError(f'Incompatible version. This feature is no longer available after TPP {maximum}.')

    class _Timeout:
        def __init__(self, timeout):
            self.timeout = timeout
            self.max_time = timeout + time.time()

        def __enter__(self):
            logger.set_rule(
                log_tag=LogTags.feature,
                min_tag_value=LogTags.feature.value,
                why=f'Disabling all logs during timeout to reduce redundant logging.'
            )
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            logger.set_rule(
                log_tag=LogTags.feature,
                reset=True,
                why=f'Enabling all logs after timeout.'
            )
            return

        def is_expired(self, poll: float = 0.5):
            time.sleep(poll)
            return time.time() >= self.max_time


class _FeatureException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def log(self):
        logger.log(
            msg=self.__str__(),
            log_tag=LogTags.critical,
            num_prev_callers=2
        )


class FeatureError(_FeatureException):
    def __init__(self, msg):
        super().__init__(msg)

    class InvalidFormat(_FeatureException):
        pass

    class InvalidResultCode(_FeatureException):
        def __init__(self, code: int, code_description: str = 'Unknown'):
            super().__init__(f'Expected a valid result code, but got "{code}": {code_description}.')

    class TimeoutError(_FeatureException):
        def __init__(self, method, expected_value, actual_value, timeout: int):
            super().__init__(
                f'{method.__name__} did not return {expected_value} in {timeout} seconds. Got {actual_value} instead.')

    class UnexpectedValue(_FeatureException):
        pass

"""
pytpp.features.certificate.get('\VED\Policy\...')
pytpp.features.perrmissions.assign(policy='\VED\Policy', identity='local:tyler')
pytpp.features.perrmissions.assign(policy='{12341234}', identity='local:tyler')
"""
