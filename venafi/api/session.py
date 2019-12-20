import requests
import json


class Session:
    """
    This class is responsible for holding the appropriate headers to authenticate each
    request. It also removes all null values from all data sent to TPP.
    """
    def __init__(self, headers: dict):
        self.headers = headers
        self.requests = requests
        self.requests.packages.urllib3.disable_warnings()

    def post(self, url: str, data: dict, verify: bool = False):
        """
        Sends a POST request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data
            verify: Validate the endpoint's TLS Server Certificate when ``True``.

        Returns:
            Returns the raw response returned by the server.
        """
        data = self._remove_null_values_from_dictionary(d=data)
        return self.requests.post(url=url, data=json.dumps(data), headers=self.headers, verify=verify)

    def get(self, url: str, params: dict = None, verify: bool = False):
        """
        Sends a GET request to the given URL with the given URL parameters.

        Args:
            url: URL endpoint
            params: Dictionary of parameters to append to the URL
            verify: Validate the endpoint's TLS Server Certificate when ``True``.

        Returns:
            Returns the raw response returned by the server.
        """
        params = self._remove_null_values_from_dictionary(d=params)
        return self.requests.get(url=url, params=params, headers=self.headers, verify=verify)

    def delete(self, url: str, verify: bool = False):
        """
        Sends a DELETE request to the given URL.

        Args:
            url: URL endpoint
            verify: Validate the endpoint's TLS Server Certificate when ``True``.

        Returns:
            Returns the raw response returned by the server.
        """
        return self.requests.delete(url, headers=self.headers, verify=verify)

    def put(self, url: str, data: dict, verify: bool = False):
        """
        Sends a PUT request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data
            verify: Validate the endpoint's TLS Server Certificate when ``True``.

        Returns:
            Returns the raw response returned by the server.
        """
        data = self._remove_null_values_from_dictionary(d=data)
        return self.requests.put(url=url, data=json.dumps(data), headers=self.headers, verify=verify)

    def _remove_null_values_from_dictionary(self, d: dict):
        """
        Removes all values that are of NoneType recursively within a dictionary.
        """
        if not isinstance(d, dict):
            return d

        for key, value in list(d.items()):
            if value is None:
                del d[key]
            elif isinstance(value, dict):
                self._remove_null_values_from_dictionary(value)
        return d
