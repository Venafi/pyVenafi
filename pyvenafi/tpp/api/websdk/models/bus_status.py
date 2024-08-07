from __future__ import annotations

from datetime import datetime

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class AdditionalProp(ObjectModel):
    mesh_dns_name: str = ApiField(alias='MeshDnsName')
    engine_identity: str = ApiField(alias='EngineIdentity')
    unreachable_bus_partners: list[str] = ApiField(alias='UnreachableBusPartners')
    current_latency: int = ApiField(alias='CurrentLatency')
    current_workload: int = ApiField(alias='CurrentWorkload')
    standby_mode: int = ApiField(alias='StandbyMode')
    loaded_modules: list[str] = ApiField(alias='LoadedModules')
    process_type: str = ApiField(alias='ProcessType')
    process_id: int = ApiField(alias='ProcessId')
    process_identity: str = ApiField(alias='ProcessIdentity')
    start_time_iso_8601: str = ApiField(alias='StartTimeISO8601')
    last_seen_iso_8601: str = ApiField(alias='LastSeenISO8601')
    sending_host: str = ApiField(alias='SendingHost')
    sending_application: str = ApiField(alias='SendingApplication')
    no_response: bool = ApiField(alias='NoResponse')

class AdditionalPropStatus(ObjectModel):
    additional_prop_1: AdditionalPropStatus = ApiField(alias='additionalProp1')
    additional_prop_2: AdditionalPropStatus = ApiField(alias='additionalProp2')
    additional_prop_3: AdditionalPropStatus = ApiField(alias='additionalProp3')

class Status(ObjectModel):
    reporting_engine: str = ApiField(alias='ReportingEngine')
    mesh: bool = ApiField(alias='Mesh')
    mesh_port: int = ApiField(alias='MeshPort')
    status: str = ApiField(alias='Status')
    status_last_updated_iso_8601: datetime = ApiField(alias='StatusLastUpdatedISO8601')
