import requests
import json
from logger import logger, LogLevels
from config import settings as s


WEBSDK_URL = 'https://{host}/vedsdk'.format(host=s.TPP_HOST)
APERTURE_URL = 'https://{host}/aperture/api'.format(host=s.TPP_HOST)
requests.packages.urllib3.disable_warnings()


class Session:
    def __init__(self, headers):
        self.headers = headers

    def post(self, url: str, data: dict, verify: bool = False):
        data = json.dumps(data, indent=4)
        logger.log(f'{url}: {data}', level=LogLevels.api, prev_frames=2)
        return requests.post(url=url, data=data, headers=self.headers, verify=verify)

    def get(self, url: str, params: dict = None, verify: bool = False):
        if params:
            pretty_params = json.dumps(params, indent=4)
            logger.log(f'{url}: {pretty_params}', level=LogLevels.api, prev_frames=2)
        else:
            logger.log(url, level=LogLevels.api, prev_frames=2)
        return requests.get(url=url, params=params, headers=self.headers, verify=verify)

    def delete(self, url: str, verify: bool = False):
        logger.log(url, level=LogLevels.api, prev_frames=2)
        return requests.delete(url, headers=self.headers, verify=verify)

    def put(self, url: str, data: dict, verify: bool = False):
        data = json.dumps(data, indent=4)
        logger.log(f'{url}: {data}', level=LogLevels.api, prev_frames=2)
        return requests.put(url=url, data=data, headers=self.headers, verify=verify)
