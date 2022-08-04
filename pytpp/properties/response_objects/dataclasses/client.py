from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List, Literal


ClientType = Literal['VenafiAgent', 'AgentJuniorMachine', 'AgentJuniorUser', 'Portal', 'Agentless',
                     'PreEnrollment', 'iOS', 'Android']
OSNameType = Literal['AIX', 'Android', 'BlackBerry', 'BSD', 'HPux', 'iOS', 'Linux', 'MacOS', 'Other',
                     'Solaris', 'Unknown', 'Windows', 'zOS']
WorkType = Literal['Client Agent Configuration Work', 'Client Agent Automatic Upgrade Work',
                   'Client Agent Device Placement Work', 'Certificate Provisioning Work', 'Client Agent SSH Discovery Work',
                   'Client Agent SSH Provisioning Work', 'Client Agent SSH Key Usage Work', 'Client User Certificate Work',
                   'Client Certificate Work']


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def client_result(self) -> str:
        return ResultCodes.Client.get(self.code, 'Unknown')


class Work(PayloadModel):
    associated_groups: List[str] = PayloadField(alias='AssociatedGroups')
    work_dn: str = PayloadField(alias='WorkDn')
    work_name: str = PayloadField(alias='WorkName')
    work_type: WorkType = PayloadField(alias='WorkType')


class Network(PayloadModel):
    ip_address: str = PayloadField(alias='IpAddress')
    mac_address: str = PayloadField(alias='MacAddress')


class Client(PayloadModel):
    client_id: int = PayloadField(alias='ClientId')
    client_type: ClientType = PayloadField(alias='ClientType')
    fqdn: str = PayloadField(alias='Fqdn')
    os_name: OSNameType = PayloadField(alias='OsName')
    username: str = PayloadField(alias='Username')


class ClientDetails(PayloadModel):
    certificate_device: str = PayloadField(alias='CertificateDevice')
    client_id: int = PayloadField(alias='ClientId')
    client_type: ClientType = PayloadField(alias='ClientType')
    client_version: str = PayloadField(alias='ClientVersion')
    created_on: datetime = PayloadField(alias='CreatedOn')
    dns_name: str = PayloadField(alias='DnsName')
    effective_work: List[str] = PayloadField(alias='EffectiveWork')
    fqdn: str = PayloadField(alias='Fqdn')
    groups: List[str] = PayloadField(alias='Groups')
    host_domain: str = PayloadField(alias='HostDomain')
    hostname: str = PayloadField(alias='Hostname')
    last_seen_on: datetime = PayloadField(alias='LastSeenOn')
    networks: List[Network] = PayloadField(alias='Networks')
    os_build: str = PayloadField(alias='OsBuild')
    os_name: OSNameType = PayloadField(alias='OsName')
    os_service_pack: str = PayloadField(alias='OsServicePack')
    os_version: str = PayloadField(alias='OsVersion')
    region: str = PayloadField(alias='Region')
    serial_number: str = PayloadField(alias='SerialNumber')
    ssh_device: str = PayloadField(alias='SshDevice')
    system_architecture: str = PayloadField(alias='SystemArchitecture')
    system_chassis: str = PayloadField(alias='SystemChassis')
    system_manufacturer: str = PayloadField(alias='SystemManufacturer')
    system_model: str = PayloadField(alias='SystemModel')
    trust_level: str = PayloadField(alias='TrustLevel')
    username: str = PayloadField(alias='Username')
    virtual_machine_id: str = PayloadField(alias='VirtualMachineId')
