from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class ValidationBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Validation Base"
    file_validation_error = Attribute('File Validation Error', min_version='21.4')
    file_validation_result = Attribute('File Validation Result', min_version='21.4')
    last_validation = Attribute('Last Validation', min_version='21.4')
    last_validation_result = Attribute('Last Validation Result', min_version='21.4')
    ssl_listen_host = Attribute('SSL Listen Host', min_version='21.4')
    ssl_listen_port = Attribute('SSL Listen Port', min_version='21.4')
    use_specified_host = Attribute('Use Specified Host', min_version='21.4')
    validation_disabled = Attribute('Validation Disabled', min_version='21.4')
    validation_errors = Attribute('Validation Errors', min_version='21.4')
    validation_results = Attribute('Validation Results', min_version='21.4')
