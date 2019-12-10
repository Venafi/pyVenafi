from properties.resultcodes import ResultCodes


class Client:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.client_result = ResultCodes.Client.get(code, 'Unknown')

    class Client:
        def __init__(self, clients_dict: dict, api_type: str):
            if not isinstance(clients_dict, dict):
                clients_dict = {}

            if api_type.lower() == 'websdk':
                self.client_id = clients_dict.get('ClientId')
                self.client_type = clients_dict.get('ClientType')
                self.fqdn = clients_dict.get('FQDN')
                self.os_name = clients_dict.get('OsName')
                self.username = clients_dict.get('Username')

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class ClientDetails:
        def __init__(self, clients_dict: dict, api_type: str):
            if not isinstance(clients_dict, dict):
                clients_dict = {}

            if api_type.lower() == 'websdk':
                self.certificate_device = clients_dict.get('CertificateDevice')
                self.client_id = clients_dict.get('ClientId')
                self.client_type = clients_dict.get('ClientType')
                self.client_version = clients_dict.get('ClientVersion')
                self.created_on = clients_dict.get('CreatedOn')
                self.dns_name = clients_dict.get('DnsName')
                self.effective_work = clients_dict.get('EffectiveWork')
                self.fqdn = clients_dict.get('FQDN')
                self.groups = clients_dict.get('Groups')
                self.host_domain = clients_dict.get('HostDomain')
                self.hostname = clients_dict.get('Hostname')
                self.last_seen_on = clients_dict.get('LastSeenOn')
                self.networks = [Client._Network(network) for network in clients_dict.get('Networks')]
                self.os_build = clients_dict.get('OsBuild')
                self.os_name = clients_dict.get('OsName')
                self.os_service_pack = clients_dict.get('OsServicePack')
                self.os_version = clients_dict.get('OsVersion')
                self.region = clients_dict.get('Region')
                self.serial_number = clients_dict.get('SerialNumber')
                self.ssh_device = clients_dict.get('SshDevice')
                self.system_architecture = clients_dict.get('SystemArchitecture')
                self.system_chassis = clients_dict.get('SystemChassis')
                self.system_manufacturer = clients_dict.get('SystemManufacturer')
                self.system_model = clients_dict.get('SystemModel')
                self.trust_level = clients_dict.get('TrustLevel')
                self.username = clients_dict.get('Username')
                self.virtual_machine_id = clients_dict.get('VirtualMachineId')

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class Work:
        def __init__(self, work_dict: dict, api_type: str):
            if not isinstance(work_dict, dict):
                work_dict = {}
            if api_type.lower() == 'websdk':
                self.associated_groups = work_dict.get('AssociatedGroups')
                self.work_dn = work_dict.get('WorkDn')
                self.work_name = work_dict.get('WorkName')
                self.work_type = work_dict.get('WorkType')

            elif api_type.lower() == 'aperture':
                # Not implemented yet.
                pass

    class _Network:
        def __init__(self, network_dict: dict):
            if not isinstance(network_dict, dict):
                network_dict = {}

            self.ip_address = network_dict.get('IpAddress')
            self.mac_address = network_dict.get('MacAddress')
