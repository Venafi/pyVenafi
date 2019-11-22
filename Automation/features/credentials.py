from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences


class _Credential:
    pass


class UsernamePasswordCredential(FeatureBase, _Credential):
    def __init__(self, auth_obj):
        super().__init__(auth_obj)

    def load(self):
        pass

    def create(self, name: str, container: str, username: str, password: str):
        dn = container + "\\" + name

        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Credentials.Create.post(
            credential_path=dn,
            friendly_name='UsernamePassword',
            values=[
                {'Name': 'Username', 'Type': 'string', 'Value': username},
                {'Name': 'Password', 'Type': 'string', 'Value': password}
            ]
        ).result

        self._logger.log('UsernamePassword credential "%s" created successfully.' % dn)

        self.load()
        return self
