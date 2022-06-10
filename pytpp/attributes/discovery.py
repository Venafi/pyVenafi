from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.top import TopAttributes


class DiscoveryAttributes(DiscoveryStatisticsAttributes, ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    address_parsing_errors = Attribute('Address Parsing Errors', min_version='15.4')
    address_range = Attribute('Address Range')
    automatically_import = Attribute('Automatically Import')
    certificate_instances_found = Attribute('Certificate Instances Found')
    certificate_location_dn = Attribute('Certificate Location DN')
    certificates_already_known = Attribute('Certificates Already Known')
    certificates_excluded = Attribute('Certificates Excluded')
    completed = Attribute('Completed')
    completed_assignments = Attribute('Completed Assignments')
    configuration = Attribute('Configuration')
    connect_excluded = Attribute('Connect Excluded')
    creation_date = Attribute('Creation Date')
    device_location_dn = Attribute('Device Location DN')
    discovery_exclusion_dn = Attribute('Discovery Exclusion DN')
    in_progress = Attribute('In Progress')
    keys_already_known = Attribute('Keys Already Known')
    keys_excluded = Attribute('Keys Excluded')
    last_update = Attribute('Last Update', min_version='16.2')
    new_certificate_instances_found = Attribute('New Certificate Instances Found')
    new_certificates_found = Attribute('New Certificates Found')
    new_ssh_servers_found = Attribute('New SSH Servers Found', min_version='16.3')
    placement_preview = Attribute('Placement Preview')
    placement_rule = Attribute('Placement Rule')
    placement_summary = Attribute('Placement Summary')
    priority = Attribute('Priority')
    protection_key = Attribute('Protection Key')
    report_dn = Attribute('Report DN')
    resolve_host = Attribute('Resolve Host')
    ssh_servers_found = Attribute('SSH Servers Found', min_version='16.3')
    started = Attribute('Started')
    status = Attribute('Status')
    total_assignments = Attribute('Total Assignments')
    window_days_of_month = Attribute('Window Days of Month')
    window_days_of_week = Attribute('Window Days of Week')
    window_end = Attribute('Window End')
    window_start = Attribute('Window Start')
    work_units = Attribute('Work Units')
