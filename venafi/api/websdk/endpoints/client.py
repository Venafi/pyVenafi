from api.api_base import API, response_property
from properties.response_objects.client import Client


class _Client(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Client', valid_return_codes=[200, 204])
        self.Delete = self._Delete(websdk_obj=websdk_obj)
        self.Details = self._Details(websdk_obj=websdk_obj)
        self.Work = self._Work(websdk_obj=websdk_obj)

    @property
    @response_property()
    def clients(self):
        if self.response.status_code == 204:
            return []
        return [Client.Client(client, self._api_type) for client in self.json_response()]

    def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
            last_seen_on: str = None,last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
            os_name: str = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None, user_name: str = None,
            virtual_machine_id: int = None):
        params = {
            'ClientVersion': client_version,
            'ClientType': client_type,
            'HostName': host_name,
            'IpAddress': ip_address,
            'LastSeenOn': last_seen_on,
            'LastSeenOnGreater': last_seen_on_greater,
            'LastSeenOnLess': last_seen_on_less,
            'MacAddress': mac_address,
            'OSName': os_name,
            'OSVersion': os_version,
            'Region': region,
            'SerialNumber': serial_number,
            'SID': sid,
            'UserName': user_name,
            'VirtualMachineId': virtual_machine_id
        }

        self.response = self._get(params=params)

        return self

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Delete', valid_return_codes=[200])

        @property
        @response_property()
        def deleted_count(self):
            return self.json_response(key='DeletedCount')

        @property
        @response_property()
        def errors(self):
            return self.json_response(key='Errors')

        def post(self, clients: list, delete_associated_devices: bool = False):
            body = {
                'Clients': clients,
                'DeleteAssociatedDevices': delete_associated_devices
            }

            self.response = self._post(data=body)

            return self

    class _Details(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Details', valid_return_codes=[200, 204])

        @property
        @response_property()
        def details(self):
            return [Client.ClientDetails(client, self._api_type) for client in self.json_response()]

        def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
                last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
                os_name: str = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None, user_name: str = None,
                virtual_machine_id: int = None):
            params = {
                'ClientVersion': client_version,
                'ClientType': client_type,
                'HostName': host_name,
                'IpAddress': ip_address,
                'LastSeenOn': last_seen_on,
                'LastSeenOnGreater': last_seen_on_greater,
                'LastSeenOnLess': last_seen_on_less,
                'MacAddress': mac_address,
                'OSName': os_name,
                'OSVersion': os_version,
                'Region': region,
                'SerialNumber': serial_number,
                'SID': sid,
                'UserName': user_name,
                'VirtualMachineId': virtual_machine_id
            }

            self.response = self._get(params=params)

            return self

    class _Work(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Client/Work', valid_return_codes=[200, 204])

        @property
        @response_property()
        def works(self):
            return [Client.Work(work, self._api_type) for work in self.json_response()]

        def get(self):
            self.response = self._get()
            return self
