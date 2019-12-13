from properties.resultcodes import ResultCodes


class Client:
    class Result:
        def __init__(self, code: int):
            self.code = code  # type: int
            self.client_result = ResultCodes.Client.get(code, 'Unknown')

    class Client:
        def __init__(self, clients_dict: dict, api_type: str):
            if not isinstance(clients_dict, dict):
                clients_dict = {}

            if api_type.lower() == 'websdk':
                self.client_id = clients_dict.get('ClientId')  # type: int
                self.client_type = clients_dict.get('ClientType')  # type: str
                self.fqdn = clients_dict.get('FQDN')  # type: str
                self.os_name = clients_dict.get('OsName')  # type: str
                self.username = clients_dict.get('Username')  # type: str

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class ClientDetails:
        def __init__(self, clients_dict: dict, api_type: str):
            if not isinstance(clients_dict, dict):
                clients_dict = {}

            if api_type.lower() == 'websdk':
                self.certificate_device = clients_dict.get('CertificateDevice')  # type: str
                self.client_id = clients_dict.get('ClientId')  # type: int
                self.client_type = clients_dict.get('ClientType')  # type: str
                self.client_version = clients_dict.get('ClientVersion')  # type: str
                self.created_on = clients_dict.get('CreatedOn')  # type: str
                self.dns_name = clients_dict.get('DnsName')  # type: str
                self.effective_work = clients_dict.get('EffectiveWork')  # type: list
                self.fqdn = clients_dict.get('FQDN')  # type: str
                self.groups = clients_dict.get('Groups')  # type: list
                self.host_domain = clients_dict.get('HostDomain')  # type: str
                self.hostname = clients_dict.get('Hostname')  # type: str
                self.last_seen_on = clients_dict.get('LastSeenOn')  # type: str
                self.networks = [Client._Network(network) for network in clients_dict.get('Networks')]
                self.os_build = clients_dict.get('OsBuild')  # type: str
                self.os_name = clients_dict.get('OsName')  # type: str
                self.os_service_pack = clients_dict.get('OsServicePack')  # type: str
                self.os_version = clients_dict.get('OsVersion')  # type: str
                self.region = clients_dict.get('Region')  # type: str
                self.serial_number = clients_dict.get('SerialNumber')  # type: str
                self.ssh_device = clients_dict.get('SshDevice')  # type: str
                self.system_architecture = clients_dict.get('SystemArchitecture')  # type: str
                self.system_chassis = clients_dict.get('SystemChassis')  # type: str
                self.system_manufacturer = clients_dict.get('SystemManufacturer')  # type: str
                self.system_model = clients_dict.get('SystemModel')  # type: str
                self.trust_level = clients_dict.get('TrustLevel')  # type: str
                self.username = clients_dict.get('Username')  # type: str
                self.virtual_machine_id = clients_dict.get('VirtualMachineId')  # type: str

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class Work:
        def __init__(self, work_dict: dict, api_type: str):
            if not isinstance(work_dict, dict):
                work_dict = {}
            if api_type.lower() == 'websdk':
                self.associated_groups = work_dict.get('AssociatedGroups')  # type: list
                self.work_dn = work_dict.get('WorkDn')  # type: str
                self.work_name = work_dict.get('WorkName')  # type: str
                self.work_type = work_dict.get('WorkType')  # type: str

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class _Network:
        def __init__(self, network_dict: dict):
            if not isinstance(network_dict, dict):
                network_dict = {}

            self.ip_address = network_dict.get('IpAddress')  # type: str
            self.mac_address = network_dict.get('MacAddress')  # type: str
