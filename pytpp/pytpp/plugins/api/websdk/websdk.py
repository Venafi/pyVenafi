from pytpp.api.websdk.websdk import *
from pytpp.plugins.api.websdk.endpoints.rights import _Rights


class WebSDK(WebSDK):
    @logger.wrap_func(LogTags.feature, mask_input_regexes=['password', 'token'])
    def __init__(self, host: str, username: str, password: str, token: str = None, application_id: str = None,
                 scope: Union[Scope, str] = None, refresh_token: str = None, proxies: dict = None,
                 certificate_path: str = None, key_file_path: str = None, verify_ssl: bool = False):
        super().__init__(
            host=host, username=username, password=password, token=token, application_id=application_id,
            scope=scope, refresh_token=refresh_token, proxies=proxies, certificate_path=certificate_path,
            key_file_path=key_file_path, verify_ssl=verify_ssl
        )
        self.Rights = _Rights(self)
