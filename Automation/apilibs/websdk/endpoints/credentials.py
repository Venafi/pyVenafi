import json
import time, datetime
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from objects.response_objects.credential import Credentials


class _Credentials:
    def __init__(self, session, api_type):
        self.Create = self._Create(session=session, api_type=api_type)

    class _Create(API):
        def __init__(self, session, api_type):
            API.__init__(
                self,
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Credentials/Create',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            result = self.response.json().get('Result')
            result = Credentials.Result(result)
            if result.code != 1:
                raise ValueError('Could not create credential. Received %s: %s.' % (result.code, result.credential_result))
            self.logger.log('Credential object created successfully.')
            return result

        def post(self, credential_path, friendly_name, values, password=None, description=None, encrytpion_key=None, shared=False, expiration=None, contact=None):
            """
            :param credential_path: path from VED to the credential object
            :type credential_path: str
            :type password: str
            :type friendly_name: str
            :type values: list of tuple or list of list
            :type description: str
            :type encrytpion_key: str
            :type shared: bool
            :type expiration: int
            :type contact: list of Identity
            """
            payload = {
                'CredentialPath': credential_path,
                'Password': password,
                'FriendlyName': friendly_name,
            }
            if description:
                payload.update({'Description': description})

            if encrytpion_key:
                payload.update({'EncryptionKey': encrytpion_key})

            if shared:
                payload.update({'Shared': shared})

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = long((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            payload.update({'Expiration': r'/Date(%s)/' % exp_date})
            if contact:
                payload.update({'Contact': contact})

            payload.update({'Values': values})
            body = json.dumps(payload)
            self.response = self._session.post(url=self._url, data=body)

            return self
