from apilibs.base import API, response_property, InvalidResultCode
from apilibs.session import WEBSDK_URL
from objects.response_objects.config import Config


class _Config:
    def __init__(self, session, api_type):
        self.AddDnValue = self._AddDnValue(session, api_type)
        self.AddPolicyValue = self._AddPolicyValue(session, api_type)
        self.Create = self._Create(session, api_type)
        self.Delete = self._Delete(session, api_type)
        self.FindObjectsOfClass = self._FindObjectsOfClass(session, api_type)

    class _AddDnValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/AddDnValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not add DN Value. Received %s: %s.' %(result.code, result.config_result))
            self.logger.log('Successfully added DN value.')
            return result

        def post(self, object_dn, attribute_name, value):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value
            }

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _AddPolicyValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/AddPolicyValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not add Policy Value. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully added Policy value.')

        def post(self, object_dn, attribute_name, class_name, value, locked):
            return self

    class _Create(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Create',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise ValueError('An error occurred: "%s"' % result['Error'])
            self.log_json_object('Config Object', result)
            return Config.Object(result.get('Object'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise InvalidResultCode(url=self._url, code=result.code, code_desc=result.config_result)
            self.log_valid_result_code()
            return result

        def post(self, object_dn, class_name, name_attribute_list):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "NameAttributeList": name_attribute_list
            }

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Delete(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Delete',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not delete config object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, recursive):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _FindObjectsOfClass(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/FindObjectsOfClass',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Objects', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find config object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, classes=None, class_name=None, object_dn=None, pattern=None, recursive=None):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes": classes,
                "Class": class_name,
                "ObjectDN": object_dn,
                "Pattern": pattern,
                "Recursive": recursive
            }

            self.response = self._session.post(url=self._url, data=body)

            return self
