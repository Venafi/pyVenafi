import requests
import json
from logger import logger
from config import settings as s


WEBSDK_URL = 'https://{host}/vedsdk'.format(host=s.TPP_HOST)
APERTURE_URL = 'https://{host}/aperture/api'.format(host=s.TPP_HOST)
requests.packages.urllib3.disable_warnings()


class Session:
    def __init__(self, headers):
        self.headers = headers
        self._logger = logger.api_logger

    def post(self, url: str, data: dict, verify: bool = False):
        data = json.dumps(data, indent=4)
        self._logger.log('%s: %s' % (url, data), prev_frames=2)
        return requests.post(url=url, data=data, headers=self.headers, verify=verify)

    def get(self, url: str, params: dict = None, verify: bool = False):
        if params:
            self._logger.log('%s: %s' %(url, json.dumps(params, indent=4)), prev_frames=2)
        else:
            self._logger.log(url, prev_frames=2)
        return requests.get(url=url, params=params, headers=self.headers, verify=verify)

    def delete(self, url: str, verify: bool = False):
        self._logger.log(url, prev_frames=2)
        return requests.delete(url, headers=self.headers, verify=verify)

    def put(self, url: str, data: dict, verify: bool = False):
        data = json.dumps(data, indent=4)
        self._logger.log('%s: %s' % (url, data), prev_frames=2)
        return requests.put(url=url, data=data, headers=self.headers, verify=verify)
