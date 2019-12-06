import requests
import json


class Session:
    def __init__(self, headers: dict):
        self.headers = headers
        self.requests = requests
        self.requests.packages.urllib3.disable_warnings()

    def post(self, url: str, data: dict, verify: bool = False):
        return self.requests.post(url=url, data=json.dumps(data), headers=self.headers, verify=verify)

    def get(self, url: str, params: dict = None, verify: bool = False):
        return self.requests.get(url=url, params=params, headers=self.headers, verify=verify)

    def delete(self, url: str, verify: bool = False):
        return self.requests.delete(url, headers=self.headers, verify=verify)

    def put(self, url: str, data: dict, verify: bool = False):
        return self.requests.put(url=url, data=json.dumps(data), headers=self.headers, verify=verify)
