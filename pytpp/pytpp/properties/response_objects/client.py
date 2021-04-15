from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string


class Client:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.client_result = ResultCodes.Client.get(code, 'Unknown')

    class Client:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.client_id = response_object.get('ClientId')  # type: int
            self.client_type = response_object.get('ClientType')  # type: str
            self.fqdn = response_object.get('FQDN')  # type: str
            self.os_name = response_object.get('OsName')  # type: str
            self.username = response_object.get('Username')  # type: str

    class ClientDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.certificate_device = response_object.get('CertificateDevice')  # type: str
            self.client_id = response_object.get('ClientId')  # type: int
            self.client_type = response_object.get('ClientType')  # type: str
            self.client_version = response_object.get('ClientVersion')  # type: str
            self.created_on = from_date_string(response_object.get('CreatedOn'))
            self.dns_name = response_object.get('DnsName')  # type: str
            self.effective_work = response_object.get('EffectiveWork')  # type: list
            self.fqdn = response_object.get('FQDN')  # type: str
            self.groups = response_object.get('Groups')  # type: list
            self.host_domain = response_object.get('HostDomain')  # type: str
            self.hostname = response_object.get('Hostname')  # type: str
            self.last_seen_on = from_date_string(response_object.get('LastSeenOn'))
            self.networks = [Client._Network(network) for network in response_object.get('Networks')]
            self.os_build = response_object.get('OsBuild')  # type: str
            self.os_name = response_object.get('OsName')  # type: str
            self.os_service_pack = response_object.get('OsServicePack')  # type: str
            self.os_version = response_object.get('OsVersion')  # type: str
            self.region = response_object.get('Region')  # type: str
            self.serial_number = response_object.get('SerialNumber')  # type: str
            self.ssh_device = response_object.get('SshDevice')  # type: str
            self.system_architecture = response_object.get('SystemArchitecture')  # type: str
            self.system_chassis = response_object.get('SystemChassis')  # type: str
            self.system_manufacturer = response_object.get('SystemManufacturer')  # type: str
            self.system_model = response_object.get('SystemModel')  # type: str
            self.trust_level = response_object.get('TrustLevel')  # type: str
            self.username = response_object.get('Username')  # type: str
            self.virtual_machine_id = response_object.get('VirtualMachineId')  # type: str

    class Work:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.associated_groups = response_object.get('AssociatedGroups')  # type: list
            self.work_dn = response_object.get('WorkDn')  # type: str
            self.work_name = response_object.get('WorkName')  # type: str
            self.work_type = response_object.get('WorkType')  # type: str

    class _Network:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.ip_address = response_object.get('IpAddress')  # type: str
            self.mac_address = response_object.get('MacAddress')  # type: str
