from pytpp.api.api_base import OutputModel, ApiField


class Self(OutputModel):
    href: str = ApiField(alias='Href')


class Link(OutputModel):
    self: Self = ApiField(alias='Self')


class Engine(OutputModel):
    links: Link = ApiField(alias='_links')
    engine_dn: str = ApiField(alias='EngineDn')
    engine_guid: str = ApiField(alias='EngineGuid')
    engine_name: str = ApiField(alias='EngineName')


class Folder(OutputModel):
    folder_dn: str = ApiField(alias='FolderDN')
    folder_guid: str = ApiField(alias='FolderGuid')
    folder_name: str = ApiField(alias='FolderName')
