from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class TreeRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Tree Root"
    company_name = Attribute('Company Name')
    migration_task = Attribute('Migration Task')
    pendo_eula_version = Attribute('Pendo EULA Version')
    pendo_optional_data_collection = Attribute('Pendo Optional Data Collection')
    schema_version = Attribute('Schema Version')
    usage_tracking = Attribute('Usage Tracking')
    use_company_name_for_analytics = Attribute('Use Company Name for Analytics')
    version = Attribute('Version')
