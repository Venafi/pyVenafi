from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    client_result: str = PayloadField(alias='ClientResult', default=None)


class Client(PayloadModel):
    client_id: int = PayloadField(alias='ClientId', default=None)
    client_type: str = PayloadField(alias='ClientType', default=None)
    fqdn: str = PayloadField(alias='Fqdn', default=None)
    os_name: str = PayloadField(alias='OsName', default=None)
    username: str = PayloadField(alias='Username', default=None)


class ClientDetails(PayloadModel):
    certificate_device: str = PayloadField(alias='CertificateDevice', default=None)
    client_id: int = PayloadField(alias='ClientId', default=None)
    client_type: str = PayloadField(alias='ClientType', default=None)
    client_version: str = PayloadField(alias='ClientVersion', default=None)
    created_on: datetime = PayloadField(alias='CreatedOn', default=None)
    dns_name: str = PayloadField(alias='DnsName', default=None)
    effective_work: list = PayloadField(alias='EffectiveWork', default=None)
    fqdn: str = PayloadField(alias='Fqdn', default=None)
    groups: list = PayloadField(alias='Groups', default=None)
    host_domain: str = PayloadField(alias='HostDomain', default=None)
    hostname: str = PayloadField(alias='Hostname', default=None)
    last_seen_on: datetime = PayloadField(alias='LastSeenOn', default=None)
    networks: 'List[_Network]' = PayloadField(alias='Networks', default=None)
    os_build: str = PayloadField(alias='OsBuild', default=None)
    os_name: str = PayloadField(alias='OsName', default=None)
    os_service_pack: str = PayloadField(alias='OsServicePack', default=None)
    os_version: str = PayloadField(alias='OsVersion', default=None)
    region: str = PayloadField(alias='Region', default=None)
    serial_number: str = PayloadField(alias='SerialNumber', default=None)
    ssh_device: str = PayloadField(alias='SshDevice', default=None)
    system_architecture: str = PayloadField(alias='SystemArchitecture', default=None)
    system_chassis: str = PayloadField(alias='SystemChassis', default=None)
    system_manufacturer: str = PayloadField(alias='SystemManufacturer', default=None)
    system_model: str = PayloadField(alias='SystemModel', default=None)
    trust_level: str = PayloadField(alias='TrustLevel', default=None)
    username: str = PayloadField(alias='Username', default=None)
    virtual_machine_id: str = PayloadField(alias='VirtualMachineId', default=None)


class Work(PayloadModel):
    associated_groups: list = PayloadField(alias='AssociatedGroups', default=None)
    work_dn: str = PayloadField(alias='WorkDn', default=None)
    work_name: str = PayloadField(alias='WorkName', default=None)
    work_type: str = PayloadField(alias='WorkType', default=None)


class _Network(PayloadModel):
    ip_address: str = PayloadField(alias='IpAddress', default=None)
    mac_address: str = PayloadField(alias='MacAddress', default=None)
